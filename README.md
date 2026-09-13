 # 🛡️ Sentinel AI — Financial Fraud Detection & Investigation System

Sentinel AI is an AI-assisted financial fraud detection and investigation system designed to identify potentially suspicious financial transactions, assign risk levels, visualize transaction behavior, and provide AI-generated explanations for flagged transactions.

The project combines statistical anomaly detection, risk scoring, interactive visualization, and Generative AI to help analysts understand and prioritize potentially suspicious activity.

---

## 🚨 Problem Statement

Financial systems process a large number of transactions every day, making it difficult to manually identify unusual or potentially suspicious activity.

Manual monitoring can be time-consuming because analysts need to:

- Examine large volumes of transactions
- Identify unusual transaction amounts
- Prioritize high-risk transactions
- Understand why a transaction was flagged
- Determine which transactions require further investigation

**Sentinel AI addresses this problem by automatically analyzing transactions, detecting statistical anomalies, calculating risk scores, and providing AI-assisted explanations for suspicious activity.**

---

## 💡 Solution

Sentinel AI provides an end-to-end fraud investigation workflow:

```text
Transaction Data
       ↓
Statistical Anomaly Detection
       ↓
Risk Scoring
       ↓
Risk Classification
       ↓
Threat Queue
       ↓
Investigation Center
       ↓
AI Investigator
       ↓
Explanation & Recommended Verification
````

The system helps an analyst move from a large transaction dataset to prioritized suspicious transactions and understandable AI-assisted investigation results.

---

## ✨ Key Features

### 🔎 Statistical Anomaly Detection

Uses **Z-score analysis** to identify transaction amounts that significantly differ from the normal transaction distribution.

### 🎯 Risk Scoring

Suspicious transactions receive a risk score from **0–100** and are classified into:

* 🟢 LOW
* 🟡 MODERATE
* 🟠 HIGH
* 🔴 CRITICAL

### 📊 Interactive Risk Dashboard

Provides visual analysis of:

* Transaction statistics
* Risk landscape
* Risk distribution
* Transaction amount vs risk
* Complete transaction dataset

### 🚨 Threat Queue

Displays flagged transactions and prioritizes them according to their calculated risk score.

### 🔍 Investigation Center

Allows analysts to select and inspect individual suspicious transactions, including:

* Transaction ID
* Account
* Transaction type
* Amount
* Z-score
* Risk score
* Risk level

### 🤖 AI Investigator

Uses an LLM-powered investigator to provide:

* Explanation of why a transaction may be suspicious
* Explanation of the Z-score
* Recommended verification steps

The AI assists the analyst and does not independently declare that a transaction is fraudulent.

### 📈 Interactive Data Visualization

Uses Plotly to visualize transaction risk patterns and distributions.

### 📥 CSV Export

Allows the analyzed transaction dataset to be downloaded as a CSV file.

### 🎨 Modern User Interface

Includes a custom futuristic dashboard with:

* 3D-style background
* Glassmorphism cards
* Neon visual effects
* Risk indicators
* Responsive layout

---

## 🖥️ Application Screenshots

### 🚀 Initial Dashboard

The initial dashboard allows the user to configure the number of transactions and start the fraud detection analysis.

<img src="screenshots/01-start-screen.png" alt="Sentinel AI Initial Dashboard" width="900">

---

### 📊 Dashboard & Risk Analytics

The Overview dashboard provides the transaction risk landscape, risk distribution, amount-versus-risk analysis, and transaction dataset.

<img src="screenshots/02-overview-analytics.png" alt="Sentinel AI Risk Analytics Dashboard" width="900">

---

### 🚨 Threat Queue

The Threat Queue displays suspicious transactions and prioritizes them based on their calculated risk level and risk score.

<img src="screenshots/04-threat-queue.png" alt="Sentinel AI Threat Queue" width="900">

---

### 🔎 Investigation Center & AI Investigator

The Investigation Center allows analysts to select a suspicious transaction, inspect its risk signals and transaction details, and generate an AI-powered investigation.

<img src="screenshots/03-investigation-center.png" alt="Sentinel AI Investigation Center" width="900">

---

## 🧠 Technology Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| Python        | Core application development           |
| Pandas        | Data processing and analysis           |
| NumPy         | Numerical and statistical calculations |
| Streamlit     | Interactive web dashboard              |
| Plotly        | Data visualization                     |
| LangChain     | LLM application integration            |
| Groq          | AI inference                           |
| Python-dotenv | Environment variable management        |
| Git & GitHub  | Version control                        |

---

## 🏗️ Project Structure

```text
sentinel-ai-fraud-detection/
│
├── app.py
├── transaction_data.py
├── fraud_detector.py
├── risk_engine.py
├── explain_fraud.py
│
├── ui/
│   ├── __init__.py
│   ├── components.py
│   ├── charts.py
│   └── styles.css
│
├── screenshots/
│   ├── 01-start-screen.png
│   ├── 02-overview-analytics.png
│   ├── 03-investigation-center.png
│   └── 04-threat-queue.png
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

### 1. Transaction Generation

The system generates simulated financial transactions containing:

* Transaction ID
* Amount
* Transaction type
* Account

Unusually large transaction amounts are introduced to simulate anomalous activity.

### 2. Anomaly Detection

The system calculates the **Z-score** of transaction amounts.

Transactions with unusually high deviations from the normal distribution are flagged for investigation.

### 3. Risk Engine

The risk engine evaluates transaction characteristics and generates a **risk score between 0 and 100**.

The transaction is then assigned a risk level such as LOW, MODERATE, HIGH, or CRITICAL.

### 4. Threat Prioritization

Flagged transactions are sorted by risk score so that higher-risk transactions can be investigated first.

### 5. Investigation

The analyst selects a suspicious transaction from the Investigation Center and reviews its transaction details and risk signals.

### 6. AI Analysis

The selected transaction is sent to the AI Investigator.

The AI provides an explanation of the suspicious behavior and recommended verification steps to support human investigation.

---

## 🚀 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/sentinel-ai-fraud-detection.git
```

### 2. Open the project

```bash
cd sentinel-ai-fraud-detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Groq API

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 7. Run the application

```bash
streamlit run app.py
```

The Sentinel AI dashboard will open in your browser.

---

## 🔐 Environment Variables

The application requires a Groq API key for the AI Investigator.

Create:

```text
.env
```

and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

A `.env.example` file is included as a configuration template.

The actual `.env` file is excluded from Git using `.gitignore`.

**Never commit your real API key to GitHub.**

---

## ⚠️ Limitations

This project is an educational/demo fraud detection system using simulated transaction data and statistical anomaly detection.

A flagged transaction represents **potentially suspicious activity** and does not prove that fraud has occurred.

The current risk score is a project-level scoring mechanism and should not be interpreted as a calibrated probability of fraud.

The AI Investigator is designed to assist human analysis rather than make autonomous financial or fraud decisions.

---

## 🔮 Future Improvements

Possible future enhancements include:

* Account behavioral profiling
* Transaction velocity detection
* Machine learning-based fraud classification
* Real-world transaction datasets
* Network and relationship analysis
* Analyst feedback and human-in-the-loop learning
* PDF investigation reports
* Authentication and role-based access
* Cloud deployment

---

## 👨‍💻 Author

**TARUNREDDY**

Student project demonstrating the integration of:

**Data Analytics • Python • Statistics • Generative AI • Financial Fraud Detection**

---

## ⭐ Disclaimer

## ⚠️ Disclaimer

This project is intended for educational and demonstration purposes only.

It uses simulated transaction data and is not intended to replace professional financial fraud detection systems, banking security controls, or financial crime investigation processes.

This version is the one I'd use for your GitHub portfolio. It is detailed enough to explain the project, but not so long that someone has to read a huge document before understanding what **Sentinel AI** does.
