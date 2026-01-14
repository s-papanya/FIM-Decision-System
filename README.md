# FIM-Decision-System

![Status](https://img.shields.io/badge/Status-Active_Development-brightgreen)
![Tech Stack](https://img.shields.io/badge/Stack-Wazuh_%7C_Vector_%7C_Redis_%7C_Python-blue)

## 📖 Executive Summary
This project re-engineers the traditional Wazuh SIEM pipeline to address the industry-wide challenge of **"Alert Fatigue."** By replacing standard log shippers with **Vector (Rust-based)** and implementing an **Event-Driven Architecture** with Redis, this system transforms noisy, raw security alerts into actionable, high-fidelity incidents.

The core objective is to decouple the **Detection Layer** (Wazuh) from the **Decision Layer** (Custom Engine), allowing for advanced correlation logic that significantly improves the Signal-to-Noise Ratio (SNR) for SOC operations.

## 🏗️ System Architecture
The pipeline implements an **Event-Driven Architecture** designed for reliability and efficiency. By decoupling log ingestion from processing using **Redis**, the system ensures **data resilience** during traffic spikes and enables **custom correlation logic**
## 🏗 Architecture Diagram
```mermaid
graph LR
    subgraph Endpoints [Monitored Infrastructure]
        A1[Linux Server] -->|Secure Log Forwarding| M
        A2[Windows Station] -->|Secure Log Forwarding| M
        A3[Network Devices] -->|Syslog| M
    end

    subgraph Server [Wazuh Server Instance]
        M[Wazuh Manager]
        F[File: alerts.json]
        V[Vector Agent]
        
        M -->|Analysis & Correlation| F
        F -->|Read/Tail| V
    end

    subgraph Processing [Decision Pipeline]
        V -->|Stream| R[(Redis Buffer)]
        R -->|Pull| D[Custom Decision Engine]
    end
    
    subgraph Storage [Long-term]
        V -->|Bulk Index| I[(Wazuh Indexer)]
    end

    style M fill:#f9f,stroke:#333
    style F fill:#eee,stroke:#333,stroke-dasharray: 5 5
    style V fill:#ff9,stroke:#333,stroke-width:2px
    style D fill:#bfb,stroke:#333
