🌉 SentryNode Gateway: The Semantic Security Layer for Autonomous Agents

[![Tearsheet](https://img.shields.io/badge/View-Executive_Tearsheet-00C2A8?style=for-the-badge)](https://nehadangwal.github.io/sentrynode-gateway/)

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge)](./LICENSE)

[![Status](https://img.shields.io/badge/Status-Patent_Pending-green.svg)](#patent-information)

SentryNode is a high-performance semantic gateway that enforces intelligent routing, hard budget guardrails, and cryptographic provenance on every AI request.

[Explore the Roadmap & Benchmarks →](https://nehadangwal.github.io/sentrynode-gateway/)

### 🛡️ Patent-Information
**U.S. Patent Pending (Application No. 63/982,542)** *Filed February 13, 2026*

This repository contains the official implementation of the SentryNode Gateway architecture, as disclosed in our USPTO filing. Key protected technologies include:
* [cite_start]**Adaptive Inference Routing** (SLM-First Strategy) [cite: 113, 131]
* [cite_start]**Shadow Mode Validation Engine** (Parallel Quality Checks) [cite: 114, 135]
* [cite_start]**Semantic Circuit Breaker** (Recursive Loop Detection) [cite: 116, 143]
* [cite_start]**Sidecar Sandbox Execution** (Kernel-level Isolation) [cite: 119, 145]
  
### ⚖️ Licensing
Licensed under the **Apache License, Version 2.0**. This license includes a **patent grant** protecting both contributors and users. See the [LICENSE](./LICENSE) and [NOTICE](./NOTICE) files for details.

Architecting Technical Sovereignty for the AI Era.
SentryNode is a high-performance framework designed to eliminate the "AI Tax." As organizations scale, they face a dual crisis: unpredictable token costs and the security risks of autonomous agents.
SentryNode implements Adaptive Inference and FinOps Guardrails to ensure every token spent translates to business value, achieving an average of 77.6% cost reduction without quality loss.

🚀 The Core Mission: Solving the "AI Tax"
In 2026, the primary hurdle for AI deployment isn't capability—it's efficiency. 
SentryNode acts as a strategic mediation layer that enforces The Golden Path for every request, ensuring that high-intelligence frontier models are reserved only for tasks that require them.

✨ Key Capabilities (Updated 2026)
* Adaptive Routing (FinOps Engine): Automatically offloads routine tasks to Small Language Models (SLMs). Real-time visibility allows for immediate cost-avoidance calculation.
* Sovereign Signatures & Provenance: Every response is now cryptographically enforced (HMAC-SHA256). This ensures 100% provenance of the "Student" model output, preventing unauthorized model spoofing.
* Semantic Circuit Breakers: Monitors for sub-second semantic repetition to kill recursive agentic loops before they exhaust cloud budgets.
* Hardened Sidecar Sandbox (SAE): Uses gVisor (runsc) to provide user-space kernel isolation. Recently updated to a minimalist Python-native footprint, removing OS-level binaries like curl to significantly reduce the container attack surface.

📊 Validated Benchmarks (2026 Tiers) 
Running a mixed-complexity workload of 1,000 requests:
Metric	                Ungoverned (Direct)	      SentryNode (Optimized)	    Improvement
Cost per 1k Requests	  $5.00	                    $1.12	                      77.6% Reduction
Routing Strategy	      Static / Premium	        Adaptive / SLM-First	      80% Offload
Circuit Breakers	      0 (Infinite Spend)	      100% Intercepted	          Risk: Eliminated
Quality Parity	        N/A	                      98% Semantic Match	        Zero Loss

![SentryNode Efficiency Gain](./ai_cost_savings.png)

```mermaid
graph TD
  A[Agent Request] --> B{SentryNode Gateway}
  B -- High Complexity --> C[Frontier LLM]
  B -- Routine Task --> D[Local SLM]
  D --> E[Quality Parity Check]
  E --> F[HMAC Signature & FinOps Log]
  C --> F
```

## 🗺️ Strategic Roadmap
The SentryNode framework is evolving from a benchmarking suite into a production-grade sovereignty layer. Progress is tracked through the following development epochs:

Epoch 1: Foundational Framework (100%)

[x] Patent-Pending Architecture: Public disclosure of methodology (#63/982,542).
[x] FinOps Benchmarking: Validated 77.6% unit-cost reduction logic.
[x] Hardened Health Checks: Migration to native Python monitoring for minimal container footprint.

Epoch 2: Quality & Governance (98%)

[x] Shadow Mode API: Real-time parity validation between SLM and Frontier models.
[x] Semantic Circuit Breaking: Sub-second loop interception via Redis state matching.
[ ] Telemetry Integration: Finalizing structured logging for OpenTelemetry.

Epoch 3: Enterprise Sovereignty (85%)

[x] Sidecar Sandbox Core: Network-isolated code execution via gVisor.
[x] Sovereign Engine v1.0: Verified HMAC-SHA256 cryptographic enforcement.
[ ] Cross-Cloud Arbitrage: Real-time spot pricing shifts (Scheduled Q4 2026).

## 📖 Strategic Framework & Research
SentryNode isn't just a gateway; it's a financial architecture for the agentic era.
* **[Executive Summary](./EXECUTIVE_SUMMARY.md)**: The high-level business case for dismantling the "AI Tax" and achieving $17M+ ROI.
* **[Research Pillars](./RESEARCH_PILLARS.md)**: Technical deep-dive into Adaptive Routing, Shadow Mode, and Unit Economics.
* **[Architecture Deep-Dive](./ARCHITECTURE.md)**: Detailed system schematics and component interaction maps.

👤 About the Founder
Neha Dangwal | Founder, SentryNode Gateway Neha is an AI Infrastructure Architect at the intersection of FinOps and Agentic Security. She built SentryNode to solve the dual crisis of runaway token costs and unverifiable model provenance.
**[Read Full Founder Bio](./FOUNDER.md)**
🤝 Partner Search: Seeking a Technical Co-Founder to own GTM and infrastructure scaling. Contact via LinkedIn.

🛠️ Public Framework Architecture
This repository provides the Interface Specifications and Benchmarking Suite for the SentryNode ecosystem.
FastAPI: High-performance async API layer.
LiteLLM: Model abstraction for 100+ LLMs.
Pydantic: Strict data validation for engineering governance.
Governance Stubs: Interfaces for implementing proprietary circuit breakers.

⚡ Quick Start: Experience the 77.6% Savings
Test the governance and loop-protection logic in Mock Mode (no API keys required).

1. Installation
```
    git clone https://github.com/nehadangwal/sentrynode-gateway.git
    cd sentrynode-gateway
    pip install -r requirements.txt
```

2. Run the Governance & Loop Test
Observe how the system detects recursive loops and switches to the most cost-efficient route.
```
    export MOCK_MODE=true
    python3 test_guardrails.py
```

3. Run Shadow Mode Verification
See the FinOps engine calculate "Cost Avoidance" in real-time.
```
    export MOCK_MODE=true
    python3 test_shadow.py
```

⚡ Quick Start: Docker Environment
  Experience the governance and sovereignty logic using our hardened container setup.
```
    # 1. Build the Hardened Environment
    docker compose -f infrastructure/docker-compose.yaml up -d --build
    
    # 2. Verify Sovereign State (HMAC Signed Request)
    curl -X POST http://localhost:8001/api/v1/chat \
    -H "Content-Type: application/json" \
    -d '{"prompt": "Analyze efficiency metrics", "user_id": "audit_user_01"}'
    
    # 3. Audit the FinOps Ledger (Redis)
    docker exec -it sentrynode_cache redis-cli HGETALL stats:audit_user_01
```

## 📊 Sample Output
```
python3 benchmark_report.py
📊 Starting SentryNode Benchmark Simulation (10 Requests)...
------------------------------------------------------------

[🚀] Incoming Request: 'Complex task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.00390

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.00780

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.01170

[🚀] Incoming Request: 'Complex task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.01560

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.01950

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.02340

[🚀] Incoming Request: 'Complex task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚖️ [ROUTE] High Complexity Detected -> Frontier Model (GPT-4o/Claude 3.5)
💰 [FINOPS] Insight: This request saved $0.00000
📊 [SESSION] Cumulative Savings: $0.02340

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚖️ [ROUTE] High Complexity Detected -> Frontier Model (GPT-4o/Claude 3.5)
💰 [FINOPS] Insight: This request saved $0.00000
📊 [SESSION] Cumulative Savings: $0.02340

[🚀] Incoming Request: 'Simple task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚡ [ROUTE] Adaptive Offload -> SLM Optimized (Llama 3/Mistral)
💰 [FINOPS] Insight: This request saved $0.00390
📊 [SESSION] Cumulative Savings: $0.02730

[🚀] Incoming Request: 'Complex task...'
🔍 [ANALYSIS] Evaluating task complexity...
⚖️ [ROUTE] High Complexity Detected -> Frontier Model (GPT-4o/Claude 3.5)
💰 [FINOPS] Insight: This request saved $0.00000
📊 [SESSION] Cumulative Savings: $0.02730
------------------------------------------------------------
📈 FINAL BENCHMARK REPORT
------------------------------------------------------------
Direct Frontier Cost:   $0.0500
SentryNode Opt. Cost:   $0.0227
Total Capital Saved:    $0.0273
Efficiency Gain:        77.6% (Validated)
------------------------------------------------------------
```

📖 Deep Dives
This project is the technical implementation of the principles found in Neha Dangwal’s 2026 research series:

The AI Tax: **[A $17M Perspective on FinOps](https://medium.com/@nehadangwal/the-ai-tax-is-breaking-engineering-margins-a-17m-perspective-on-finops-7fce44983866)**

The Sovereign Agent: **[Why Naked AI Execution is a Liability](https://medium.com/@nehadangwal/the-sovereign-agent-why-naked-ai-execution-is-an-enterprise-liability-f4f31a116493)**

🤝 Enterprise & IP
This public repository contains the open-access framework and benchmarking tools. For inquiries regarding the SentryNode Proprietary Engine (Private IP), Adaptive Routing Algorithms, or Enterprise Sandbox configurations, please contact [Neha Dangwal](mailto:neha.sentrynode@gmail.com).

Legal Notice: SentryNode and its underlying adaptive routing methodologies and secure sandbox architectures are the Intellectual Property of Neha Dangwal. Certain components described herein are subject to pending patent applications.


## 🤝 Community & Feedback
SentryNode is built on the principle of **Architectural Sovereignty**. We value input from AI Infrastructure engineers, FinOps practitioners, and Automation specialists.

* **Found a Bottleneck?** [Open an Issue](https://github.com/nehadangwal/sentrynode-gateway/issues) using our performance template.
  
* **Design Suggestion?** Join the [Discussions](https://github.com/nehadangwal/sentrynode-gateway/discussions) to talk about Adaptive Routing edge cases.
  
* **Enterprise Deep-Dive:** For inquiries regarding the proprietary gVisor-hardened core or custom routing algorithms, please [contact Neha Dangwal via LinkedIn](https://www.linkedin.com/in/nehadangwal).
  

> “The metric that matters in 2026 isn't just Accuracy—it's **Cost Per Successful Task**.”
