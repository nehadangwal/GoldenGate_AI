# governance.py
from fastapi import HTTPException
import time

# Enhanced Simulated Database with Velocity Tracking
PROJECT_BUDGETS = {
    "marketing_team": {
        "limit": 50.0, 
        "spent": 48.50, 
        "velocity_limit_per_min": 1.0, # Max $1/min
        "last_spend_time": 0
    },
    "engineering_research": {
        "limit": 500.0, 
        "spent": 120.0, 
        "velocity_limit_per_min": 10.0,
        "last_spend_time": 0
    }
}

def check_budget(project_id: str):
    if project_id not in PROJECT_BUDGETS:
        raise HTTPException(status_code=404, detail="Project ID not registered.")
    
    project = PROJECT_BUDGETS[project_id]
    
    # 1. Total Budget Check
    if project["spent"] >= project["limit"]:
        raise HTTPException(status_code=402, detail="Monthly AI Budget Exceeded.")

    # 2. Velocity Circuit Breaker (New Guardrail)
    current_time = time.time()
    time_since_last = (current_time - project["last_spend_time"]) / 60
    
    # If requests are coming in faster than the velocity limit allows
    if time_since_last < 0.01: # Detects sub-second recursive loops
         print(f"CRITICAL: High-velocity loop detected for {project_id}!")
         # In a real system, you'd trigger an alert here
         
    return True

def log_usage(project_id: str, cost: float):
    PROJECT_BUDGETS[project_id]["spent"] += cost
    PROJECT_BUDGETS[project_id]["last_spend_time"] = time.time()
    print(f"INFO: {project_id} spent ${cost:.4f}. Total: ${PROJECT_BUDGETS[project_id]['spent']:.2f}")