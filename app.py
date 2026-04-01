import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Flight Delay System", page_icon="✈️")

# -------- SESSION --------
if "users" not in st.session_state:
    st.session_state.users = {"admin": "flight123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# -------- LOGIN BACKGROUND (AIRPLANE AI LIGHT) --------
def login_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1529070538774-1843cb3265df");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


# -------- DASHBOARD BACKGROUND (AIRPLANE DARK) --------
def dashboard_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109cc05");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


# -------- REGISTER PAGE --------
if st.session_state.page == "register":

    login_bg()

    st.title("✈ Create Account")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")

    if st.button("Register"):
        if username in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[username] = password
            st.success("Account created successfully")

    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()


# -------- LOGIN PAGE --------
elif not st.session_state.login:

    login_bg()

    st.title("✈ AI Flight Delay Prediction")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid Username or Password")

    if st.button("Register New Account"):
        st.session_state.page = "register"
        st.rerun()


# -------- DASHBOARD --------
else:

    dashboard_bg()

    st.title("✈ Flight Delay Prediction Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        dep_airport = st.selectbox(
            "Departure Airport",
            ["Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad"]
        )

    with col2:
        arr_airport = st.selectbox(
            "Arrival Airport",
            ["Dubai", "Singapore", "London", "New York", "Tokyo"]
        )

    airline = st.selectbox(
        "Airline",
        ["IndiGo", "Air India", "SpiceJet", "Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear", "Rain", "Storm", "Fog"]
    )

    date = st.date_input("Flight Date")

    time = st.slider("Departure Hour", 0, 23)

    if st.button("Predict Flight Delay"):

        delay = random.randint(0, 100)

        st.subheader("Prediction Result")

        st.progress(delay)

        if delay > 60:
            st.error(f"⚠ High Delay Probability: {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay Probability: {delay}%")
        else:
            st.success(f"Low Delay Probability: {delay}%")

        est = random.randint(10, 120)
        st.info(f"Estimated Delay Time: {est} minutes")

        chart = pd.DataFrame({
            "Status": ["Delay", "On Time"],
            "Value": [delay, 100 - delay]
        })

        st.bar_chart(chart.set_index("Status"))

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
