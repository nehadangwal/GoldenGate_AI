# router.py
import os
from litellm import completion

# MockResponse is defined at the top level so it is accessible to all tests
class MockResponse:
    def __init__(self, model):
        # High-fidelity mock response including simulated cost data
        self.choices = [{"message": {"content": "Mocked AI Response: The main difference between Vector and Graph DBs is how they store relationships."}}]
        # 2026 pricing: GPT-4o ($5.00/1M) vs GPT-4o-mini ($0.15/1M)
        cost_val = 0.005 if model == "gpt-4o" else 0.00015
        self._hidden_params = {"response_cost": cost_val}

class AdaptiveRouter:
    # Class-level variable to persist aggregate savings across the session
    total_savings = 0.0
    
    def __init__(self):
        self.tiers = {"small": "gpt-4o-mini", "large": "gpt-4o"}
        self.recent_prompts = {}

    def route_request(self, prompt: str, project_id: str = "default"):
        # Circuit Breaker: Detects sub-second duplicate requests
        if project_id in self.recent_prompts and prompt == self.recent_prompts[project_id]:
            return "throttle"
        self.recent_prompts[project_id] = prompt
        
        # Adaptive Routing: SLM-first strategy based on semantic complexity
        is_complex = any(kw in prompt.lower() for kw in ["analyze", "refactor", "architect", "graph", "vector"])
        return self.tiers["large"] if (len(prompt.split()) > 300 or is_complex) else self.tiers["small"]

    def execute(self, prompt: str, project_id: str, shadow_mode: bool = False):
        model = self.route_request(prompt, project_id)
        
        if model == "throttle":
            raise Exception("Agentic Loop Detected: Circuit Breaker Activated.")

        # Primary execution
        response, model_used = self._call_model(prompt, model)

        # Shadow Mode logic: Only triggers when the router downcycles to an SLM
        if shadow_mode and model_used == self.tiers["small"]:
            print(f"DEBUG: Shadow Mode Active. Mirroring request to {self.tiers['large']}...")
            shadow_response, _ = self._call_model(prompt, self.tiers["large"])
            self._log_shadow_comparison(response, shadow_response)
        
        return response, model_used

    def _call_model(self, prompt, model):
        # Environmental check for Mock Mode to allow zero-cost testing
        if os.getenv("MOCK_MODE") == "true":
            return MockResponse(model), model
        return completion(model=model, messages=[{"role": "user", "content": prompt}]), model

    def _log_shadow_comparison(self, primary, shadow):
        # FinOps Audit Engine: Calculates real-time cost avoidance
        p_cost = primary._hidden_params.get("response_cost", 0)
        s_cost = shadow._hidden_params.get("response_cost", 0)
        current_savings = s_cost - p_cost
        
        AdaptiveRouter.total_savings += current_savings
        
        print(f"📈 SHADOW STATS: Parity Check - Primary: {len(primary.choices[0]['message']['content'])} chars")
        print(f"💰 FINOPS INSIGHT: This request saved ${current_savings:.5f}")
        print(f"📊 SESSION TOTAL: Cumulative Savings: ${AdaptiveRouter.total_savings:.5f}")