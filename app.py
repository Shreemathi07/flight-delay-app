import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Flight Delay System", page_icon="✈️")

# -------- SESSION --------
if "users" not in st.session_state:
    st.session_state.users = {"admin":"flight123"}

if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "login"


# -------- LOGIN BACKGROUND (PERFECT FLIGHT AI) --------
def login_bg():
    st.markdown("""
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1504196606672-aef5c9cefc92");
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


# -------- DASHBOARD BACKGROUND (AIRPORT REAL) --------
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


# -------- REGISTER --------
if st.session_state.page == "register":

    login_bg()
    st.title("✈ Create Account")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Register"):
        if u in st.session_state.users:
            st.error("User already exists")
        else:
            st.session_state.users[u] = p
            st.success("Account created")

    if st.button("Back to Login"):
        st.session_state.page = "login"
        st.rerun()


# -------- LOGIN --------
elif not st.session_state.login:

    login_bg()
    st.title("✈ AI Flight Delay System")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        if u in st.session_state.users and st.session_state.users[u] == p:
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid login")

    if st.button("Register New"):
        st.session_state.page = "register"
        st.rerun()


# -------- DASHBOARD --------
else:

    dashboard_bg()
    st.title("✈ Flight Delay Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        dep = st.selectbox("Departure", ["Chennai","Delhi","Mumbai","Bangalore"])

    with col2:
        arr = st.selectbox("Arrival", ["Dubai","London","Singapore","Tokyo"])

    airline = st.selectbox("Airline", ["IndiGo","Air India","Vistara"])
    weather = st.selectbox("Weather", ["Clear","Rain","Fog","Storm"])
    time = st.slider("Departure Hour",0,23)

    if st.button("Predict Delay"):

        prob = random.randint(0,100)
        st.progress(prob)

        if prob > 60:
            st.error(f"⚠ High Delay: {prob}%")
        elif prob > 30:
            st.warning(f"Moderate Delay: {prob}%")
        else:
            st.success(f"Low Delay: {prob}%")

        delay_time = random.randint(10,120)
        st.info(f"Estimated Delay: {delay_time} minutes")

        chart = pd.DataFrame({
            "Status":["Delay","On Time"],
            "Value":[prob,100-prob]
        })

        st.bar_chart(chart.set_index("Status"))

    if st.button("Logout"):
        st.session_state.login = False
        st.rerun()
