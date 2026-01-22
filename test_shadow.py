# test_shadow.py
import os
from router import AdaptiveRouter

def run_verified_tests():
    # Force Mock Mode for testing
    os.environ["MOCK_MODE"] = "true"
    router = AdaptiveRouter()

    # TEST 1: Complex Routing (Should use Large Model)
    print("--- TEST 1: COMPLEX ROUTING ---")
    router.execute("Architect a Graph DB for RAG", "p1", shadow_mode=True)
    
    print("\n" + "-"*30 + "\n")

    # TEST 2: Simple Routing (Should use Small Model + Shadow)
    print("--- TEST 2: FINOPS SAVINGS & SHADOW MODE ---")
    router.execute("Hello, how are you?", "p2", shadow_mode=True)

if __name__ == "__main__":
    run_verified_tests()