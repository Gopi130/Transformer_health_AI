from datetime import datetime
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Transformer Health AI",
    page_icon="⚡",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}
current_time = datetime.now()

st.info(f"🕒 System Time: {current_time}")
h1, h2, h3 {
    color: #00FFFF;
}

.stButton>button {
    background-color: #00FFFF;
    color: black;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("⚡ SMART TRANSFORMER HEALTH AI SYSTEM")

st.markdown("---")

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

data = pd.read_csv("data.csv")

X = data.drop("Condition", axis=1)
y = data["Condition"]

model = RandomForestClassifier()

model.fit(X, y)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    ["Dashboard", "DGA Analysis", "IR Analysis"]
)

# ---------------------------------------------------
# DASHBOARD
# ---------------------------------------------------

if menu == "Dashboard":

    st.header("📊 Transformer Monitoring Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Transformers Active", "24")

    with col2:
        st.metric("Healthy Units", "20")

    with col3:
        st.metric("Critical Units", "4")

    st.markdown("---")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.metric("🌡 Temperature", "78°C")

    with col5:
        st.metric("⚡ Voltage", "33KV")

    with col6:
        st.metric("🛢 Oil Status", "Normal")
# ---------------------------------------------------
# DGA ANALYSIS
# ---------------------------------------------------

elif menu == "DGA Analysis":

    st.header("🧪 DGA GAS ANALYSIS")

    col1, col2 = st.columns(2)

    with col1:
        h2 = st.number_input("Hydrogen")
        ch4 = st.number_input("Methane")
        c2h2 = st.number_input("Acetylene")

    with col2:
        c2h4 = st.number_input("Ethylene")
        c2h6 = st.number_input("Ethane")
        co = st.number_input("Carbon Monoxide")

    if st.button("Predict Transformer Health"):

        prediction = model.predict([[h2, ch4, c2h2, c2h4, c2h6, co]])

        # HEALTH SCORE

        health_score = 100

        health_score -= (h2 / 100)
        health_score -= (ch4 / 100)

        if health_score < 0:
            health_score = 0

        # RESULT

        st.subheader("📈 AI Prediction Result")

        if prediction[0] == "Normal":
            st.success("✅ Transformer Condition: NORMAL")

        elif prediction[0] == "Caution":
            st.warning("⚠ Transformer Condition: CAUTION")

        elif prediction[0] == "Abnormal":
            st.error("⚠ Transformer Condition: ABNORMAL")

        else:
            st.error("🚨 Transformer Condition: DANGER")

        st.info(f"💡 Transformer Health Score: {health_score:.2f}%")
        st.progress(int(health_score))
        # ---------------------------------------------------
        # GAUGE METER
        # ---------------------------------------------------

        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=health_score,
            title={'text': "Transformer Health"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "green"},
                'steps': [
                    {'range': [0, 40], 'color': "red"},
                    {'range': [40, 70], 'color': "yellow"},
                    {'range': [70, 100], 'color': "green"}
                ]
            }
        ))

        st.plotly_chart(fig_gauge, use_container_width=True)

        # ---------------------------------------------------
        # BAR CHART
        # ---------------------------------------------------

        gas_data = {
            "Gas": [
                "Hydrogen",
                "Methane",
                "Acetylene",
                "Ethylene",
                "Ethane",
                "CO"
            ],
            "Value": [
                h2,
                ch4,
                c2h2,
                c2h4,
                c2h6,
                co
            ]
        }

        df = pd.DataFrame(gas_data)

        fig_bar = px.bar(
            df,
            x="Gas",
            y="Value",
            title="DGA Gas Distribution"
        )

        st.plotly_chart(fig_bar, use_container_width=True)

        # ---------------------------------------------------
        # PIE CHART
        # ---------------------------------------------------

        fig_pie = px.pie(
            df,
            names="Gas",
            values="Value",
            title="Gas Contribution Analysis"
        )

        st.plotly_chart(fig_pie, use_container_width=True)

        # ---------------------------------------------------
        # AI RECOMMENDATIONS
        # ---------------------------------------------------

        st.subheader("🛠 AI Recommendations")
        st.markdown("---")

        st.subheader("⚠ Fault Summary")

        if h2 > 800:
            st.write("• Partial discharge detected")

        if c2h2 > 50:
            st.write("• Arcing fault suspected")

        if co > 700:
            st.write("• Insulation degradation suspected")
        if c2h2 > 50:
            st.warning("⚠ Possible arcing fault detected.")

        if co > 700:
            st.warning("⚠ Paper insulation degradation suspected.")

        if h2 > 800:
            st.warning("⚠ Partial discharge activity detected.")

        if prediction[0] == "Danger":
            st.error("🚨 Immediate transformer inspection required.")

# ---------------------------------------------------
# IR ANALYSIS
# ---------------------------------------------------

elif menu == "IR Analysis":

    st.header("⚡ Insulation Resistance Analysis")

    kv = st.number_input("Transformer KV Rating")

    ir = st.number_input("Measured IR Value")

    required_ir = kv + 1

    st.info(f"Required Minimum IR Value: {required_ir} Mega Ohms")

    if st.button("Check IR Status"):

        if ir >= required_ir:

            st.success("✅ IR Value is GOOD")

        else:

            st.error("❌ IR Value is LOW")

            st.warning("⚠ Insulation condition may be weak.")
            st.markdown("---")

st.markdown(
    "© 2026 SMART TRANSFORMER HEALTH AI SYSTEM | Developed using Python & Streamlit"
)