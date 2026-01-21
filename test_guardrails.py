# test_guardrails.py
from router import AdaptiveRouter
from governance import check_budget, log_usage
import time

def simulate_agentic_workflow():
    router = AdaptiveRouter()
    project_id = "engineering_research"
    loop_prompt = "Refactor the authentication module using best practices."

    print(f"--- STARTING GUARDRAIL TEST FOR: {project_id} ---")

    # TEST 1: Valid Request
    print("\n[Test 1] Executing valid initial request...")
    try:
        check_budget(project_id)
        response, model = router.execute(loop_prompt, project_id)
        log_usage(project_id, 0.05) # Simulated cost
        print(f"✅ Success: Routed to {model}")
    except Exception as e:
        print(f"❌ Unexpected Failure: {e}")

    # TEST 2: High-Velocity Recursive Loop
    # We send the exact same prompt immediately after.
    print("\n[Test 2] Simulating high-velocity recursive loop...")
    try:
        check_budget(project_id)
        # This should trigger the "throttle" in router.py
        response, model = router.execute(loop_prompt, project_id)
        log_usage(project_id, 0.05)
    except Exception as e:
        print(f"🔥 Guardrail Triggered: {e}")

if __name__ == "__main__":
    simulate_agentic_workflow()