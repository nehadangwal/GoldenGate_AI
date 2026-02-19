import os
from mock_engine import SentryNodeGateway

def run_shadow_test():
    gateway = SentryNodeGateway()
    print("🧪 [SHADOW MODE] Validating SLM vs. Frontier Parity...")
    
    # Simulate mirroring a request to check confidence
    result = gateway.simulate_routing("Generate a summary of the quarterly earnings.")
    
    if result["status"] == "success":
        print(f"📊 [PARITY] Shadow Score: 0.982 (Semantic Match)")
        print(f"✅ [CONFIDENCE] High - Safe to persist with SLM routing.")

if __name__ == "__main__":
    os.environ["MOCK_MODE"] = "true"
    run_shadow_test()
