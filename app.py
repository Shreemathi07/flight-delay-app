import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Flight Delay System", page_icon="✈️")

# -------- SESSION --------
if "users" not in st.session_state:
    st.session_state.users = {"admin": "flight123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# -------- LOGIN BACKGROUND (ONLY AIRPLANE CLEAN) --------
def login_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1502920917128-1aa500764cbd");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .block-container {
        background: rgba(0,0,0,0.65);
        padding: 40px;
        border-radius: 15px;
        max-width: 400px;
        margin: auto;
    }

    h1, h2, h3, label {
        color: white;
        text-align: center;
    }

    </style>
    """, unsafe_allow_html=True)


# -------- DASHBOARD BACKGROUND (AIRPLANE) --------
def dashboard_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1494415859740-21e878dd929d");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


# -------- REGISTER PAGE --------
if st.session_state.page == "register":

    login_bg()

    st.title("✈ Create Account")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Register"):
        if user in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[user] = pwd
            st.success("Account created")

    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()


# -------- LOGIN PAGE --------
elif not st.session_state.login:

    login_bg()

    st.title("✈ Flight Delay System")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user in st.session_state.users and st.session_state.users[user] == pwd:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid login")

    if st.button("Create Account"):
        st.session_state.page = "register"
        st.rerun()


# -------- DASHBOARD --------
else:

    dashboard_bg()

    st.title("✈ Flight Delay Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        dep = st.selectbox("Departure Airport",
                           ["Chennai", "Delhi", "Mumbai", "Bangalore", "Hyderabad"])

    with col2:
        arr = st.selectbox("Arrival Airport",
                           ["Dubai", "Singapore", "London", "New York", "Tokyo"])

    airline = st.selectbox("Airline",
                           ["IndiGo", "Air India", "SpiceJet", "Vistara"])

    weather = st.selectbox("Weather",
                           ["Clear", "Rain", "Storm", "Fog"])

    date = st.date_input("Flight Date")
    time = st.slider("Departure Hour", 0, 23)

    if st.button("Predict Delay"):

        delay = random.randint(0, 100)

        st.subheader("Result")
        st.progress(delay)

        if delay > 60:
            st.error(f"⚠ High Delay: {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay: {delay}%")
        else:
            st.success(f"Low Delay: {delay}%")

        est = random.randint(10, 120)
        st.info(f"Estimated Delay: {est} minutes")

        df = pd.DataFrame({
            "Status": ["Delay", "On Time"],
            "Value": [delay, 100-delay]
        })

        st.bar_chart(df.set_index("Status"))

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
