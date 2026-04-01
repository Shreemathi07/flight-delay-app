import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Flight Delay Prediction", page_icon="✈️")

# Background image
st.markdown("""
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1504196606672-aef5c9cefc92");
background-size: cover;
}
</style>
""", unsafe_allow_html=True)

# User login database
users = {
"admin": "flight123",
"pilot": "sky456",
"control": "tower789"
}

# Session login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# LOGIN PAGE
if not st.session_state.logged_in:

    st.title("✈ AI Flight Delay Prediction System")
    st.subheader("Login to continue")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username in users and users[username] == password:
            st.session_state.logged_in = True
            st.success("Login successful! Please refresh if needed.")
        else:
            st.error("Invalid username or password")

# MAIN APP
else:

    st.title("✈ Flight Delay Prediction Dashboard")

    airport = st.selectbox(
        "Select Airport",
        ["Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad"]
    )

    airline = st.selectbox(
        "Select Airline",
        ["IndiGo", "Air India", "SpiceJet", "Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear", "Rain", "Storm", "Fog"]
    )

    departure = st.slider("Departure Time (Hour)", 0, 23)

    if st.button("Predict Delay"):

        delay = random.randint(0,100)

        st.subheader("Prediction Result")

        if delay > 60:
            st.error(f"⚠ High Delay Probability: {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay Probability: {delay}%")
        else:
            st.success(f"Low Delay Probability: {delay}%")

        chart_data = pd.DataFrame({
            "Status": ["Delay", "On Time"],
            "Percentage": [delay, 100-delay]
        })

        st.bar_chart(chart_data.set_index("Status"))
