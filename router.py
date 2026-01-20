# router.py
import os
from litellm import completion

class AdaptiveRouter:
    def __init__(self):
        # Define our model tiers
        self.tiers = {
            "small": "gpt-4o-mini",   # $0.15 / 1M tokens
            "large": "gpt-4o"         # $5.00 / 1M tokens
        }

    def route_request(self, prompt: str):
        # Logic: If prompt is > 500 words or mentions 'complex/code/logic', use Large model.
        # Otherwise, default to Small.
        word_count = len(prompt.split())
        complexity_keywords = ["analyze", "refactor", "architect", "legal"]
        
        is_complex = any(kw in prompt.lower() for kw in complexity_keywords)
        
        selected_model = self.tiers["large"] if (word_count > 300 or is_complex) else self.tiers["small"]
        return selected_model

    def execute(self, prompt: str):
        model = self.route_request(prompt)
        print(f"DEBUG: Routing to {model}")
        response = completion(model=model, messages=[{"role": "user", "content": prompt}])
        return response, model