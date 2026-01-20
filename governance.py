# governance.py
from fastapi import HTTPException

# Simulated Database
PROJECT_BUDGETS = {
    "marketing_team": {"limit": 50.0, "spent": 48.50},
    "engineering_research": {"limit": 500.0, "spent": 120.0}
}

def check_budget(project_id: str):
    if project_id not in PROJECT_BUDGETS:
        raise HTTPException(status_code=404, detail="Project ID not registered.")
    
    project = PROJECT_BUDGETS[project_id]
    if project["spent"] >= project["limit"]:
        raise HTTPException(status_code=402, detail="Monthly AI Budget Exceeded. Contact FinOps.")
    return True

def log_usage(project_id: str, cost: float):
    PROJECT_BUDGETS[project_id]["spent"] += cost
    print(f"INFO: {project_id} spent ${cost:.4f}. Total: ${PROJECT_BUDGETS[project_id]['spent']:.2f}")