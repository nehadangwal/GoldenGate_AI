```mermaid
graph TB
    subgraph Client_Layer ["🌐 Agentic Application"]
        A[Agent / User Request]
    end

    subgraph Gateway_Layer ["🛡️ Governance & Routing Layer\nPatent Pending · U.S. #63/982,542"]
        B[Cost Governance]
        C[Quality Assurance]
        D[Security Enforcement]
    end

    subgraph Intelligence_Layer ["🧠 Intelligence Layer"]
        E[Adaptive Model Selection\n77.6% cost reduction · 98.2% quality parity]
    end

    subgraph Sovereign_Layer ["🔒 Sovereign Execution Layer"]
        F[Hardened Execution Environment\nCryptographic Provenance · Kernel Isolation]
    end

    subgraph Output_Layer ["📤 Client Response"]
        G["✅ Verified · Audited · Governed"]
        H["❌ Threat Intercepted"]
    end

    %% ── High-level flow only ───────────────────────────
    A --> Gateway_Layer
    Gateway_Layer --> Intelligence_Layer
    Intelligence_Layer --> Sovereign_Layer
    Sovereign_Layer --> G
    Gateway_Layer -->|"Threat Detected"| H

    %% ── Styling ────────────────────────────────────────
    classDef gateway fill:#EEEDFE,stroke:#534AB7,color:#26215C
    classDef intel fill:#E6F1FB,stroke:#185FA5,color:#042C53
    classDef sovereign fill:#FAECE7,stroke:#993C1D,color:#4A1B0C
    classDef output_ok fill:#EAF3DE,stroke:#3B6D11,color:#173404
    classDef output_block fill:#FCEBEB,stroke:#A32D2D,color:#501313
    classDef client fill:#F1EFE8,stroke:#5F5E5A,color:#2C2C2A

    class B,C,D gateway
    class E intel
    class F sovereign
    class G output_ok
    class H output_block
    class A client
    ```
