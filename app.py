import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Flight Delay System", page_icon="✈️")

# -------- Session Storage --------
if "users" not in st.session_state:
    st.session_state.users = {"admin":"flight123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# -------- LOGIN BACKGROUND --------
def login_background():
    st.markdown("""
    <style>
    .stApp {
    background-image: url("https://images.unsplash.com/photo-1504196606672-aef5c9cefc92");
    background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)


# -------- DASHBOARD BACKGROUND --------
def dashboard_background():
    st.markdown("""
    <style>
    .stApp {
    background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109cc05");
    background-size: cover;
    }
    </style>
    """, unsafe_allow_html=True)


# ---------------- REGISTER PAGE ----------------
if st.session_state.page == "register":

    login_background()

    st.title("✈ Create Account")

    new_user = st.text_input("Create Username")
    new_pass = st.text_input("Create Password", type="password")

    if st.button("Register"):

        if new_user in st.session_state.users:
            st.error("User already exists")

        else:
            st.session_state.users[new_user] = new_pass
            st.success("Account created successfully")

    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()


# ---------------- LOGIN PAGE ----------------
elif not st.session_state.login:

    login_background()

    st.title("✈ AI Flight Delay Prediction")

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


# ---------------- DASHBOARD ----------------
else:

    dashboard_background()

    st.title("✈ Flight Delay Prediction Dashboard")

    airport = st.selectbox(
        "Airport",
        ["Chennai","Delhi","Mumbai","Bangalore","Hyderabad"]
    )

    airline = st.selectbox(
        "Airline",
        ["IndiGo","Air India","SpiceJet","Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear","Rain","Storm","Fog"]
    )

    departure = st.slider("Departure Hour",0,23)

    if st.button("Predict Delay"):

        delay = random.randint(0,100)

        st.subheader("Prediction Result")

        if delay > 60:
            st.error(f"⚠ High Delay Probability: {delay}%")

        elif delay > 30:
            st.warning(f"Moderate Delay Probability: {delay}%")

        else:
            st.success(f"Low Delay Probability: {delay}%")

        chart = pd.DataFrame({
            "Status":["Delay","On Time"],
            "Percentage":[delay,100-delay]
        })

        st.bar_chart(chart.set_index("Status"))

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
