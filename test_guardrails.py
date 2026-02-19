import os
import time
from mock_engine import SentryNodeGateway

def run_public_demo():
    # Initialize the Mock Engine (Your Public Interface)
    gateway = SentryNodeGateway()
    
    print("="*50)
    print("🌉 SentryNodeGateway: PUBLIC GOVERNANCE DEMO")
    print("="*50)
    
    # Scenario A: Standard Efficiency Task
    print("\n[SCENARIO A] Routine Data Categorization")
    gateway.simulate_routing("Categorize 500 support tickets by sentiment.")

    # Scenario B: High-Complexity Reasoning
    print("\n[SCENARIO B] Strategic Architecture Analysis")
    gateway.simulate_routing("Draft a 10-page technical migration plan for a legacy bank.")

    # Scenario C: The Agentic Loop (The Money Pit)
    print("\n[SCENARIO C] Detection of Recursive Agentic Drift")
    print("Attempting to run a recursive prompt loop...")
    time.sleep(1)
    gateway.simulate_routing("Repeat this process and loop back to start.")

    print("\n" + "="*50)
    print("✅ DEMO COMPLETE")
    print("Goal: 77.6% Cost Reduction via Adaptive Routing.")
    print("Status: Governance Active.")
    print("="*50)

if __name__ == "__main__":
    # Safety check: Default to mock mode in public repo
    os.environ["MOCK_MODE"] = "true"
    run_public_demo()
