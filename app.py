import streamlit as st

from transaction_data import generate_transactions
from fraud_detector import flag_anomalies
from risk_engine import add_risk_scores
from explain_fraud import explain_transaction

from ui.components import (
    load_css,
    show_header,
    show_metric,
    show_threat_card,
    show_investigation_header,
    show_signal
)

from ui.charts import (
    risk_landscape,
    risk_distribution,
    amount_vs_risk
)


# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Sentinel AI | Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)


# ==================================================
# LOAD DESIGN
# ==================================================

load_css()
show_header()


# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.markdown("## 🛡️ Sentinel AI")

    st.caption(
        "Intelligent Financial Threat Detection"
    )

    st.divider()

    st.markdown("### Analysis Controls")

    transaction_count = st.slider(
        "Transactions",
        min_value=50,
        max_value=500,
        value=100,
        step=50
    )

    if st.button(
        "🚀 Run Analysis",
        use_container_width=True
    ):

        # Generate transaction data
        df = generate_transactions(transaction_count)

        # Detect anomalies
        df = flag_anomalies(df)

        # Calculate risk scores
        df = add_risk_scores(df)

        # Save analysis in session
        st.session_state["df"] = df

        # Clear previous AI explanation
        st.session_state.pop(
            "explanation",
            None
        )

        st.session_state.pop(
            "explanation_id",
            None
        )

        st.success(
            "Analysis completed"
        )

    st.divider()

    st.markdown("### System Status")

    st.success(
        "● Detection Engine Online"
    )

    st.success(
        "● AI Investigator Online"
    )

    st.success(
        "● Data Pipeline Online"
    )


# ==================================================
# WAIT FOR ANALYSIS
# ==================================================

if "df" not in st.session_state:

    st.info(
        "👈 Configure the transaction count and click "
        "**Run Analysis** to start fraud detection."
    )

    st.stop()


# ==================================================
# LOAD DATA
# ==================================================

df = st.session_state["df"]


# ==================================================
# FLAGGED TRANSACTIONS
# ==================================================

flagged_df = df[
    df["Flagged"] == True
].copy()


flagged_df = flagged_df.sort_values(
    by="Risk Score",
    ascending=False
)


# ==================================================
# DASHBOARD METRICS
# ==================================================

total_transactions = len(df)

flagged_transactions = len(
    flagged_df
)

critical_count = len(
    flagged_df[
        flagged_df["Risk Level"] == "CRITICAL"
    ]
)

high_count = len(
    flagged_df[
        flagged_df["Risk Level"] == "HIGH"
    ]
)

average_risk = round(
    df["Risk Score"].mean(),
    1
)


# ==================================================
# SECURITY OVERVIEW
# ==================================================

st.markdown(
    "## Security Overview"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    show_metric(
        "Transactions",
        f"{total_transactions}",
        "",
        "Transactions analyzed"
    )


with col2:

    show_metric(
        "Threats Detected",
        f"{flagged_transactions}",
        "",
        "Statistical anomalies"
    )


with col3:

    show_metric(
        "Critical Threats",
        f"{critical_count}",
        "",
        "Immediate attention"
    )


with col4:

    show_metric(
        "Average Risk",
        f"{average_risk}/100",
        "",
        "Overall transaction risk"
    )


# ==================================================
# MAIN TABS
# ==================================================

overview_tab, threat_tab, investigation_tab = st.tabs(
    [
        "📊 Overview",
        "🚨 Threat Queue",
        "🔎 Investigation Center"
    ]
)


# ==================================================
# OVERVIEW
# ==================================================

with overview_tab:

    st.markdown(
        "### Risk Landscape"
    )

    st.plotly_chart(
        risk_landscape(df),
        use_container_width=True
    )


    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            "### Risk Distribution"
        )

        st.plotly_chart(
            risk_distribution(df),
            use_container_width=True
        )


    with col2:

        st.markdown(
            "### Amount vs Risk"
        )

        st.plotly_chart(
            amount_vs_risk(df),
            use_container_width=True
        )


    st.markdown(
        "### Transaction Dataset"
    )

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# THREAT QUEUE
# ==================================================

with threat_tab:

    st.markdown(
        "## 🚨 Active Threat Queue"
    )


    if flagged_df.empty:

        st.success(
            "No suspicious transactions detected."
        )

    else:

        st.caption(
            f"{flagged_transactions} suspicious "
            "transaction(s) require investigation."
        )


        for _, row in flagged_df.iterrows():

            show_threat_card(row)


# ==================================================
# INVESTIGATION CENTER
# ==================================================

with investigation_tab:

    st.markdown(
        "## 🔎 Investigation Center"
    )


    if flagged_df.empty:

        st.success(
            "There are no flagged transactions "
            "to investigate."
        )

    else:

        # ------------------------------------------
        # SELECT TRANSACTION
        # ------------------------------------------

        transaction_ids = flagged_df[
            "Transaction ID"
        ].tolist()


        selected_id = st.selectbox(
            "Select suspicious transaction",
            transaction_ids
        )


        selected_row = flagged_df[
            flagged_df["Transaction ID"] == selected_id
        ].iloc[0]


        # ------------------------------------------
        # INVESTIGATION HEADER
        # ------------------------------------------

        show_investigation_header(
            selected_row
        )


        # ------------------------------------------
        # RISK SIGNALS
        # ------------------------------------------

        st.markdown(
            "### Risk Signals"
        )


        col1, col2, col3, col4 = st.columns(4)


        with col1:

            show_signal(
                "Risk Score",
                f"{selected_row['Risk Score']}/100",
                "Overall calculated risk"
            )


        with col2:

            show_signal(
                "Risk Level",
                selected_row["Risk Level"],
                "Current threat classification"
            )


        with col3:

            show_signal(
                "Z-Score",
                f"{selected_row['Z-Score']:.2f}",
                "Amount deviation from normal"
            )


        with col4:

            show_signal(
                "Amount",
                f"${selected_row['Amount']:,.2f}",
                "Transaction value"
            )


        # ------------------------------------------
        # TRANSACTION DETAILS
        # ------------------------------------------

        st.markdown(
            "### Transaction Details"
        )


        detail_col1, detail_col2 = st.columns(2)


        with detail_col1:

            st.write(
                f"**Transaction ID:** "
                f"{selected_row['Transaction ID']}"
            )

            st.write(
                f"**Account:** "
                f"{selected_row['Account']}"
            )


        with detail_col2:

            st.write(
                f"**Type:** "
                f"{selected_row['Type']}"
            )

            st.write(
                f"**Amount:** "
                f"${selected_row['Amount']:,.2f}"
            )


        # ------------------------------------------
        # AI INVESTIGATOR
        # ------------------------------------------

        st.markdown(
            "### 🤖 AI Investigator"
        )


        explanation_key = selected_id


        if (
            "explanation" not in st.session_state
            or
            st.session_state.get(
                "explanation_id"
            ) != explanation_key
        ):

            if st.button(
                "🧠 Generate AI Investigation",
                use_container_width=True
            ):

                with st.spinner(
                    "AI investigator is analyzing "
                    "the transaction..."
                ):

                    explanation = explain_transaction(
                        selected_row
                    )


                    st.session_state[
                        "explanation"
                    ] = explanation


                    st.session_state[
                        "explanation_id"
                    ] = explanation_key


        # ------------------------------------------
        # SHOW AI RESULT
        # ------------------------------------------

        if (
            "explanation" in st.session_state
            and
            st.session_state.get(
                "explanation_id"
            ) == explanation_key
        ):

            st.markdown(
                st.session_state["explanation"]
            )


# ==================================================
# DOWNLOAD REPORT
# ==================================================

st.divider()


csv_data = df.to_csv(
    index=False
)


st.download_button(
    "⬇️ Download Analysis CSV",
    data=csv_data,
    file_name="fraud_analysis_report.csv",
    mime="text/csv"
)