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
    check_budget(req.project_id)
    
    # Pass project_id for loop detection
    response, model_used = router.execute(req.prompt, req.project_id) 
    
    cost = response._hidden_params.get("response_cost", 0)
    log_usage(req.project_id, cost)
    
    return {
        "model": model_used,
        "choices": response.choices,
        "loop_protection": "active"
    }