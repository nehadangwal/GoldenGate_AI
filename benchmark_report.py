# benchmark_report.py
import matplotlib.pyplot as plt
from router import AdaptiveRouter
import time

def run_benchmarks():
    router = AdaptiveRouter()
    
    # 1. Define our "Real World" Workload (1,000 requests)
    # 80% are simple tasks, 20% are complex engineering tasks
    workload = (["Simple task"] * 800) + (["Complex code refactor"] * 200)
    
    # 2. Define Pricing (per 1M tokens)
    COST_PREMIUM = 5.00  # GPT-4o
    COST_SLM = 0.15      # GPT-4o-mini
    
    # 3. Scenario A: Direct Access (Before)
    # Everything is hardcoded to the premium model by lazy developers.
    total_cost_before = len(workload) * (COST_PREMIUM / 1000) # Avg 1k tokens/req
    
    # 4. Scenario B: GoldenGate (After)
    # Our Adaptive Router chooses the model.
    total_cost_after = 0
    count_mini = 0
    count_large = 0
    
    for prompt in workload:
        model = router.route_request(prompt)
        if model == "gpt-4o-mini":
            total_cost_after += (COST_SLM / 1000)
            count_mini += 1
        else:
            total_cost_after += (COST_PREMIUM / 1000)
            count_large += 1

    # 5. Generate the "Staff-Level" Report
    savings = ((total_cost_before - total_cost_after) / total_cost_before) * 100
    
    print("--- BENCHMARK REPORT: GOLDENGATE AI ---")
    print(f"Total Requests: {len(workload)}")
    print(f"Routed to Mini (SLM): {count_mini}")
    print(f"Routed to Large (Frontier): {count_large}")
    print(f"Baseline Cost (Ungoverned): ${total_cost_before:.2f}")
    print(f"Optimized Cost (GoldenGate): ${total_cost_after:.2f}")
    print(f"🔥 TOTAL SAVINGS: {savings:.1f}%")

    # 6. Create the Visualization for LinkedIn
    labels = ['Ungoverned (Direct)', 'GoldenGate (Optimized)']
    costs = [total_cost_before, total_cost_after]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(labels, costs, color=['#ff4444', '#00C851'])
    plt.ylabel('Cost per 1,000 Requests ($)')
    plt.title('The "AI Tax" vs. GoldenGate Optimization')
    
    # Add labels on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'${yval:.2f}', va='bottom', ha='center', fontweight='bold')
    
    plt.savefig('ai_cost_savings.png')
    print("\n✅ Chart 'ai_cost_savings.png' generated. Ready for LinkedIn.")

if __name__ == "__main__":
    run_benchmarks()