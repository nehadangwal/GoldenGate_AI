# router.py
import os
from litellm import completion

class AdaptiveRouter:
    def __init__(self):
        self.tiers = {
            "small": "gpt-4o-mini",
            "large": "gpt-4o"
        }
        self.recent_prompts = {} 

    def route_request(self, prompt: str, project_id: str = "default"):
        if project_id in self.recent_prompts:
            if prompt == self.recent_prompts[project_id]:
                print(f"WARNING: Recursive loop detected for {project_id}. Throttling...")
                return "throttle"

        self.recent_prompts[project_id] = prompt
        
        word_count = len(prompt.split())
        complexity_keywords = ["analyze", "refactor", "architect", "legal"]
        is_complex = any(kw in prompt.lower() for kw in complexity_keywords)
        
        selected_model = self.tiers["large"] if (word_count > 300 or is_complex) else self.tiers["small"]
        return selected_model

    def execute(self, prompt: str, project_id: str):
        model = self.route_request(prompt, project_id)
        
        if model == "throttle":
            raise Exception("Agentic Loop Detected: Circuit Breaker Activated.")

        # --- NEW: MOCK MODE LOGIC ---
        if os.getenv("MOCK_MODE") == "true":
            print(f"DEBUG [MOCK]: Simulating response from {model}")
            # Creating a mock object that mimics the LiteLLM response structure
            class MockResponse:
                def __init__(self, model):
                    self.choices = [{"message": {"content": "Mocked AI Response"}}]
                    # Mocking cost based on your benchmark pricing
                    cost_val = 0.005 if model == "gpt-4o" else 0.00015
                    self._hidden_params = {"response_cost": cost_val}
            
            return MockResponse(model), model
        # -----------------------------

        print(f"DEBUG: Routing to {model}")
        response = completion(model=model, messages=[{"role": "user", "content": prompt}])
        return response, model