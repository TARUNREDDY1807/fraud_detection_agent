import plotly.graph_objects as go
import plotly.express as px


# ==================================================
# COMMON CHART SETTINGS
# ==================================================

def apply_dark_theme(fig):

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        ),
        font=dict(
            family="Arial",
            size=12
        ),
        hovermode="closest"
    )

    return fig


# ==================================================
# RISK LANDSCAPE
# ==================================================

def risk_landscape(df):

    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=df["Transaction ID"],
            y=df["Risk Score"],
            mode="lines+markers",
            name="Risk Score",

            line=dict(
                width=2
            ),

            marker=dict(
                size=7
            ),

            customdata=df[
                [
                    "Amount",
                    "Type",
                    "Account",
                    "Risk Level",
                    "Z-Score"
                ]
            ].values,

            hovertemplate=(
                "<b>%{x}</b><br>"
                "Risk Score: %{y}/100<br>"
                "Amount: $%{customdata[0]:,.2f}<br>"
                "Type: %{customdata[1]}<br>"
                "Account: %{customdata[2]}<br>"
                "Risk Level: %{customdata[3]}<br>"
                "Z-Score: %{customdata[4]:.2f}"
                "<extra></extra>"
            )
        )
    )


    fig.update_layout(
        title="Transaction Risk Landscape",
        xaxis_title="Transaction",
        yaxis_title="Risk Score",
        yaxis=dict(
            range=[0, 100]
        )
    )


    return apply_dark_theme(fig)


# ==================================================
# RISK DISTRIBUTION
# ==================================================

def risk_distribution(df):

    order = [
        "LOW",
        "MODERATE",
        "HIGH",
        "CRITICAL"
    ]


    counts = (
        df["Risk Level"]
        .value_counts()
        .reindex(
            order,
            fill_value=0
        )
        .reset_index()
    )


    counts.columns = [
        "Risk Level",
        "Count"
    ]


    fig = px.bar(
        counts,
        x="Risk Level",
        y="Count",
        text="Count"
    )


    fig.update_traces(
        textposition="outside"
    )


    fig.update_layout(
        title="Risk Level Distribution",
        xaxis_title="Risk Level",
        yaxis_title="Transactions"
    )


    return apply_dark_theme(fig)


# ==================================================
# AMOUNT VS RISK
# ==================================================

def amount_vs_risk(df):

    fig = px.scatter(
        df,
        x="Amount",
        y="Risk Score",
        color="Risk Level",

        hover_data=[
            "Transaction ID",
            "Type",
            "Account",
            "Z-Score"
        ],

        title="Transaction Amount vs Risk"
    )


    fig.update_layout(
        xaxis_title="Transaction Amount ($)",
        yaxis_title="Risk Score"
    )


    fig.update_yaxes(
        range=[0, 100]
    )


    return apply_dark_theme(fig)