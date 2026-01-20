# main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from router import AdaptiveRouter
from governance import check_budget, log_usage

app = FastAPI(title="GoldenGate AI Gateway")
router = AdaptiveRouter()

class AIRequest(BaseModel):
    project_id: str
    prompt: str

@app.post("/v1/chat/completions")
async def chat_completion(req: AIRequest):
    # 1. Enforce Governance
    check_budget(req.project_id)
    
    # 2. Adaptive Routing
    response, model_used = router.execute(req.prompt)
    
    # 3. Calculate Cost (Simplification)
    cost = response._hidden_params.get("response_cost", 0) # LiteLLM helper
    log_usage(req.project_id, cost)
    
    return {
        "model": model_used,
        "choices": response.choices,
        "cost_saved": "Estimated 90%" if model_used == "gpt-4o-mini" else "0%"
    }