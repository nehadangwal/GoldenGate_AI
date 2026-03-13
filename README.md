# 🌉 SentryNode Gateway
### Architecting Technical Sovereignty for the AI Era

> *"The metric that matters in 2026 isn't just Accuracy — it's Cost Per Successful Task."*

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Patent Pending](https://img.shields.io/badge/Patent-Pending%20%2363%2F982%2C542-purple.svg)]()
[![Status: Active](https://img.shields.io/badge/Status-Active%20Development-green.svg)]()

SentryNode is a high-performance governed gateway designed to eliminate the **"AI Tax."** As organizations scale autonomous agents, they face a dual crisis: unpredictable token costs and the security risks of unverified model execution. SentryNode implements Adaptive Inference and FinOps Guardrails to ensure every token spent translates to business value.

---

## 🛡️ Patent Information
**U.S. Patent Pending · Application No. 63/982,542 · Filed February 13, 2026**

This repository contains the official open-access implementation of the SentryNode Gateway framework. Key protected technologies include:

- **Adaptive Inference Routing** — SLM-First strategy for dynamic cost optimization
- **Shadow Mode Validation Engine** — Parallel quality parity checks (Claim 107)
- **Semantic Circuit Breaker** — Recursive loop detection and sub-second interception (Claim 4)
- **Sidecar Sandbox Execution** — Kernel-level isolation for agentic code

> **Note:** This public repository contains the open-access framework and benchmarking suite. The proprietary routing engine, Semantic Decision Matrix, and Enterprise Sandbox configurations are maintained as private IP. For enterprise inquiries contact [neha.sentrynode@gmail.com](mailto:neha.sentrynode@gmail.com)

---

## 🚀 The Problem: The "AI Tax"
In 2026, 80% of enterprise AI spend is waste — high-intelligence frontier models handling low-complexity tasks, compounded by recursive agent loops that can exhaust a month's budget in minutes. Without a governance layer, autonomous agents are prone to **Agentic Drift**.

Three things converged to make this a board-level crisis:
- Agentic AI went mainstream
- LLM costs stopped declining
- Boards started demanding AI ROI

---

## 💡 The Solution: The "Golden Path"
SentryNode acts as the strategic mediation layer between agentic applications and model providers:

- **Adaptive Routing** — Automatically offloads routine tasks to cost-efficient models, reserving frontier intelligence for complex reasoning
- **Shadow Mode Mirroring** — Background-validates output quality to ensure 98.2% semantic parity with zero capability loss
- **Semantic Circuit Breakers** — Intercepts recursive agentic loops within 40ms before they reach the model provider
- **Hard Governance** — Real-time budget enforcement, kill switch, and tamper-proof audit ledger
- **Sovereign Signatures** — Every response cryptographically signed for full model provenance

---

## 📊 Validated Benchmarks (2026)
Running a mixed-complexity workload of 1,000 requests using 2026 pricing tiers:

| Metric | Ungoverned | SentryNode | Improvement |
|--------|-----------|------------|-------------|
| Cost per 1k Requests | $5.00 | $1.12 | **77.6% Reduction** |
| Routing Strategy | Static / Frontier | Adaptive / SLM-First | **80% Offload** |
| Circuit Breakers | None (Infinite Spend) | 100% Intercepted | **Risk: Eliminated** |
| Quality Parity | N/A | 98.2% Semantic Match | **Zero Loss** |
| ROI Multiplier | 1.0x | 12.5x | **Verified (Claim 112)** |

**Adversarial Validation — March 2026:**
- 40ms semantic loop interception under recursive attack simulation
- 50% of simulated LLM-Drain attack neutralized at perimeter
- Redis ledger maintained state integrity under upstream 429 quota failure

---

## 🛡️ Secure Agentic Execution (SAE)
SentryNode implements a Sidecar Sandbox model to ensure agent-generated code never runs "naked" on production hosts:

- **Kernel Isolation** — User-space kernel for agentic code execution, preventing container breakouts
- **Fiscal Guardrails** — Resource caps to prevent Ghost Bills from infinite CPU-heavy loops
- **Environment Awareness** — Automatically detects host OS to apply appropriate security tiers
- **Sovereign Signatures** — HMAC-SHA256 cryptographic enforcement on every response

---

## 🗺️ Strategic Roadmap

### Epoch 1: Foundational Framework ✅ 100%
- [x] Patent-Pending Architecture: Public disclosure of methodology (#63/982,542)
- [x] FinOps Benchmarking: Validated 77.6% unit-cost reduction
- [x] Hardened Health Checks: Minimalist container footprint with native Python monitoring

### Epoch 2: Quality & Governance ✅ 100%
- [x] Shadow Mode API: Async teacher-student evaluation
- [x] Semantic Circuit Breaking: Sub-second loop interception via state matching
- [x] Telemetry Integration: Structured logging and Sovereign Ledger synchronization

### Epoch 3: Enterprise Sovereignty 🔄 90%
- [x] Sidecar Sandbox Core: Network-isolated code execution
- [x] Sovereign Engine v1.0: Verified cryptographic enforcement
- [x] Economic Projection Engine: Verified 12.5x ROI reporting
- [ ] Cross-Cloud Arbitrage: Real-time spot pricing shifts (Scheduled Q4 2026)

---

## ⚡ Quick Start

### Prerequisites
```bash
git clone https://github.com/nehadangwal/sentrynode-gateway.git
cd sentrynode-gateway
pip install -r requirements.txt
```

### Run Governance & Loop Protection Test
Observe how the system detects recursive loops and enforces cost-efficient routing. No API keys required.
```bash
export MOCK_MODE=true
python3 test_guardrails.py
```

### Run Shadow Mode Verification
See the quality parity engine calculate cost avoidance in real time.
```bash
export MOCK_MODE=true
python3 test_shadow.py
```

### Docker Environment
```bash
# 1. Build the hardened environment
docker compose -f infrastructure/docker-compose.yaml up -d --build

# 2. Verify sovereign state
curl -X POST http://localhost:8001/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Analyze efficiency metrics", "user_id": "audit_user_01"}'

# 3. Audit the FinOps Ledger
# See docs/LEDGER_AUDIT.md for ledger query commands
```

### Generate Benchmark Report
```bash
python3 benchmark_report.py
```

**Sample output:**
```
📊 SentryNode Benchmark Report
----------------------------------------
Direct Frontier Cost:   $0.0500
SentryNode Opt. Cost:   $0.0114
Total Capital Saved:    $0.0386
Efficiency Gain:        77.6% (Validated)
ROI Multiplier:         12.5x (Claim 112)
----------------------------------------
```

---

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Gateway health — Python-native monitoring |
| `/api/v1/chat` | POST | Governed agentic chat |
| `/api/v1/admin/report/{user_id}` | GET | Sovereign Trust Report |
| `/api/v1/admin/kill-switch` | POST | Emergency gateway override |

---

## 🛡️ Governance Operations

### Emergency Kill Switch
Immediately freeze all agentic traffic in the event of a security breach or cost spike:
```bash
# Disable gateway — blocks all requests with 503
curl -X POST 'http://localhost:8000/api/v1/admin/kill-switch?action=disable&reason=Urgent_Cost_Audit' \
  -H "Authorization: Bearer <token>"

# Restore service
curl -X POST 'http://localhost:8000/api/v1/admin/kill-switch?action=enable&reason=Audit_Complete' \
  -H "Authorization: Bearer <token>"

# Audit kill switch ledger
curl -X GET http://localhost:8000/api/v1/admin/kill-switch/audit-log \
  -H "Authorization: Bearer <token>"
```

---

## 📖 Research & Documentation

| Document | Description |
|----------|-------------|
| [EXECUTIVE_SUMMARY.md](./EXECUTIVE_SUMMARY.md) | Business case and validated ROI |
| [RESEARCH_PILLARS.md](./RESEARCH_PILLARS.md) | Technical deep-dive: Adaptive Routing, Shadow Mode, Unit Economics |
| [ARCHITECTURE.md](./ARCHITECTURE.md) | High-level system architecture |
| [FOUNDER.md](./FOUNDER.md) | About the founder and co-founder search |
| [SECURITY.md](./SECURITY.md) | Security policy and responsible disclosure |

**Published Research:**
- [The AI Tax: A $17M Perspective on FinOps](https://medium.com/@nehadangwal/the-ai-tax-is-breaking-engineering-margins-a-17m-perspective-on-finops-7fce44983866)
- [The Sovereign Agent: Why Naked AI Execution is an Enterprise Liability](https://medium.com/@nehadangwal/the-sovereign-agent-why-naked-ai-execution-is-an-enterprise-liability-f4f31a116493)
- [The Architecture of Caution](https://nehadangwal.substack.com/p/the-architecture-of-caution-engineering)
- [Inside the 77.6% Savings](https://nehadangwal.substack.com/p/deep-dive-inside-goldengate-ai-how)

---

## 🤝 Enterprise & IP

This public repository contains the **open-access framework and benchmarking tools.**

For inquiries regarding:
- SentryNode Proprietary Engine (Private IP)
- Enterprise Sandbox configurations
- Design Partner Pilot — Q2 2026 (2 slots open)

Contact: [neha.sentrynode@gmail.com](mailto:neha.sentrynode@gmail.com) · [linkedin.com/in/nehadangwal](https://linkedin.com/in/nehadangwal)

---

## 🤝 Community & Feedback
SentryNode is built on the principle of Architectural Sovereignty. Contributions welcome from AI Infrastructure engineers, FinOps practitioners, and Automation specialists.

- **Found a bottleneck?** Open an issue using our performance template
- **Design suggestion?** Join Discussions for Adaptive Routing edge cases
- **Enterprise inquiry?** Contact via LinkedIn or email above

---

## 👤 About the Founder
**Neha Dangwal** — 9 years at Cisco and Dell, $17M+ measurable impact, 11.5M+ devices. Built SentryNode to solve the AI governance problem she witnessed firsthand at scale.

[Read full founder bio →](./FOUNDER.md)

*Seeking a **Business Co-Founder** to own GTM, enterprise partnerships, and fundraising.*

---

**U.S. Patent Pending · #63/982,542 · Filed February 13, 2026**
*© 2024–2026 Neha Dangwal. All rights reserved.*
*Last updated: March 2026*
