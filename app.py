import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Flight Delay System", page_icon="✈️")

# -------- SESSION STORAGE --------
if "users" not in st.session_state:
    st.session_state.users = {"admin":"flight123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "login"

# -------- LOGIN BACKGROUND (AI Flight) --------
def login_background():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1615433590524-276fa1dc0b1c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxMTI4N3wwfDF8c2VhcmNofDF8fGFpJTIwZmxpZ2h0fGVufDB8fHx8MTY5Mzg5NzA2OQ&ixlib=rb-4.0.3&q=80&w=1080");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)

# -------- DASHBOARD BACKGROUND --------
def dashboard_background():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1502920917128-1aa500764cbd");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)

# -------- REGISTER PAGE --------
if st.session_state.page == "register":

    login_background()

    st.title("✈ Create Your Account")

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if new_user in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[new_user] = new_pass
            st.success("Account created successfully")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()

# -------- LOGIN PAGE --------
elif not st.session_state.login:

    login_background()

    st.title("✈ AI Flight Delay Prediction System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid login")

    if st.button("Register New Account"):
        st.session_state.page = "register"
        st.rerun()

# -------- DASHBOARD --------
else:

    dashboard_background()

    st.title("✈ Flight Delay Prediction Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        departure_airport = st.selectbox(
            "Departure Airport",
            ["Chennai","Delhi","Mumbai","Bangalore","Hyderabad"]
        )
    with col2:
        arrival_airport = st.selectbox(
            "Arrival Airport",
            ["Dubai","Singapore","London","New York","Tokyo"]
        )

    airline = st.selectbox(
        "Airline",
        ["IndiGo","Air India","SpiceJet","Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear","Rain","Storm","Fog"]
    )

    flight_date = st.date_input("Flight Date")
    departure_hour = st.slider("Departure Hour",0,23)

    if st.button("Predict Flight Delay"):
        delay_probability = random.randint(0,100)
        st.subheader("Prediction Result")
        st.progress(delay_probability)

        if delay_probability > 60:
            st.error(f"⚠ High Delay Probability: {delay_probability}%")
        elif delay_probability > 30:
            st.warning(f"Moderate Delay Probability: {delay_probability}%")
        else:
            st.success(f"Low Delay Probability: {delay_probability}%")

        estimated_delay = random.randint(5,120)
        st.info(f"Estimated Delay Time: {estimated_delay} minutes")

        chart = pd.DataFrame({
            "Status":["Delay","On Time"],
            "Percentage":[delay_probability,100-delay_probability]
        })
        st.bar_chart(chart.set_index("Status"))

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
