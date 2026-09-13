import streamlit as st
from pathlib import Path


# ==================================================
# LOAD CSS
# ==================================================

def load_css():

    css_path = Path(__file__).parent / "styles.css"

    if css_path.exists():
        st.html(css_path)


# ==================================================
# HEADER
# ==================================================

def show_header():

    st.html("""
        <div class="sentinel-header">

            <div class="sentinel-title">
                🛡️ SENTINEL AI
            </div>

            <div class="sentinel-subtitle">
                Intelligent Financial Fraud Detection
                &amp; Investigation Center
            </div>

        </div>

        <div class="system-online">
            ● SYSTEM ONLINE
        </div>
    """)


# ==================================================
# METRIC CARD
# ==================================================

def show_metric(
    title,
    value,
    delta,
    description
):

    st.html(f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-delta">
                {delta}
            </div>

            <div class="metric-description">
                {description}
            </div>

        </div>
    """)


# ==================================================
# THREAT CARD
# ==================================================

def show_threat_card(row):

    risk_level = str(
        row["Risk Level"]
    ).upper()

    risk_score = row["Risk Score"]

    if risk_level == "CRITICAL":
        icon = "🔴"

    elif risk_level == "HIGH":
        icon = "🟠"

    elif risk_level == "MODERATE":
        icon = "🟡"

    else:
        icon = "🟢"

    st.html(f"""
        <div class="threat-card">

            <div class="threat-header">

                <span>
                    {icon}
                    <strong>
                        {row["Transaction ID"]}
                    </strong>
                </span>

                <span class="risk-badge">
                    {risk_level}
                </span>

            </div>

            <div class="threat-details">

                <div>
                    <strong>Amount</strong>
                    <br>
                    ${row["Amount"]:,.2f}
                </div>

                <div>
                    <strong>Type</strong>
                    <br>
                    {row["Type"]}
                </div>

                <div>
                    <strong>Account</strong>
                    <br>
                    {row["Account"]}
                </div>

                <div>
                    <strong>Risk Score</strong>
                    <br>
                    {risk_score}/100
                </div>

                <div>
                    <strong>Z-Score</strong>
                    <br>
                    {row["Z-Score"]:.2f}
                </div>

            </div>

        </div>
    """)


# ==================================================
# INVESTIGATION HEADER
# ==================================================

def show_investigation_header(row):

    risk_level = str(
        row["Risk Level"]
    ).upper()

    st.html(f"""
        <div class="investigation-panel">

            <div class="investigation-title">
                🔎 Transaction Investigation
            </div>

            <div class="investigation-id">
                {row["Transaction ID"]}
            </div>

            <div class="investigation-status">
                Risk Level:
                <strong>
                    {risk_level}
                </strong>
            </div>

        </div>
    """)


# ==================================================
# RISK SIGNAL
# ==================================================

def show_signal(
    title,
    value,
    description
):

    st.html(f"""
        <div class="signal-card">

            <div class="signal-title">
                {title}
            </div>

            <div class="signal-value">
                {value}
            </div>

            <div class="signal-description">
                {description}
            </div>

        </div>
    """)