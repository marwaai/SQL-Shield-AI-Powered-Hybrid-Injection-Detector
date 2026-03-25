# 🛡️ SQL-Shield: Hybrid AI Injection Detector

**SQL-Shield** is an intelligent security layer designed to detect and block SQL Injection (SQLi) attacks. Unlike traditional firewalls that rely solely on static patterns, this project uses a **Hybrid Defense-in-Depth** architecture that combines rapid heuristic scanning with deep Machine Learning analysis.



## 🎯 The Problem
Standard Web Application Firewalls (WAFs) often struggle with:
1. **False Positives:** Blocking legitimate user text that looks like SQL.
2. **Obfuscation:** Missing attacks hidden via Hex encoding or comments (e.g., `UNI/**/ON`).
3. **Blind SQLi:** Failing to detect time-based or boolean-based logic attacks.

## 🏗️ Architecture (The 3-Layer Defense)
The system processes every input through a tiered security funnel:

1. **Stage 0: Heuristic Security Scan (Regex)**
   - Immediate blocking of high-risk patterns (Hex encoding, `UNION SELECT`, etc.).
   - **Benefit:** Extreme speed with zero CPU overhead for obvious threats.

2. **Stage 1: Structural Validation (Gatekeeper)**
   - Determines if the input is actually a SQL query or just natural language.
   - **Benefit:** Prevents the AI model from analyzing "normal chat," reducing false positives.

3. **Stage 2: Deep AI Inference (Random Forest/SVM)**
   - A trained ML model analyzes the "intent" of the SQL query.
   - **Benefit:** Detects complex **Blind SQLi** and logic-based bypasses that don't match static rules.



## 🛠️ Tech Stack
- **Languages:** Python 3.9+
- **AI/ML:** Scikit-Learn, Joblib, NLTK
- **Web Frameworks:** Streamlit (Prototype), FastAPI (Production Target)
- **DevOps:** Docker, Linux (Ubuntu/Debian)
- **Security:** Regular Expressions (Advanced Patterns)

## 🚀 Evolution: From Prototype to Production
This repository tracks the evolution of the tool:
* **v1 (Current):** Monolithic Streamlit application for rapid prototyping and UI demonstration.
* **v2 (In-Progress):** Decoupled Microservices architecture.
    * **Backend:** FastAPI service for high-concurrency inference.
    * **DevOps:** Dockerized environment for seamless Linux deployment.
    * **Logging:** SQL-Audit trail for security monitoring.

## 📊 Sample Payloads Tested
| Attack Type | Payload Example | Detection Layer |
| :--- | :--- | :--- |
| **Classic Bypass** | `' OR '1'='1' --` | Stage 0 (Regex) |
| **Hex Encoded** | `SELECT * FROM users WHERE id=0x6164...` | Stage 0 (Regex) |
| **Blind (Time)** | `1' AND SLEEP(5)--` | Stage 2 (AI Model) |
| **Boolean Logic** | `SELECT * FROM x WHERE id=1 AND 1=1` | Stage 2 (AI Model) |

## 🔧 Installation & Usage
```bash
# Clone the repo
git clone [https://github.com/yourusername/SQL-Shield.git](https://github.com/yourusername/SQL-Shield.git)

# Install dependencies
pip install -r requirements.txt

# Run the Prototype
streamlit run app.py
