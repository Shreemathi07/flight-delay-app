import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Flight Delay Prediction", page_icon="✈️")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1504196606672-aef5c9cefc92");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Login system
users = {
    "admin":"flight123",
    "pilot":"sky456",
    "control":"tower789"
}

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("✈ Flight Delay Prediction System")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]==password:
            st.session_state.login=True
            st.success("Login Successful")
        else:
            st.error("Invalid Login")

else:

    st.title("✈ Flight Delay Predictor")

    airport = st.selectbox(
        "Select Airport",
        ["Chennai","Delhi","Mumbai","Bangalore","Hyderabad"]
    )

    airline = st.selectbox(
        "Select Airline",
        ["IndiGo","Air India","SpiceJet","Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear","Rain","Storm","Fog"]
    )

    departure = st.slider("Departure Time",0,23)

    if st.button("Predict Delay"):

        delay = random.randint(0,100)

        st.subheader("Prediction Result")

        if delay > 60:
            st.error(f"⚠ High Delay Chance: {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay Chance: {delay}%")
        else:
            st.success(f"Low Delay Chance: {delay}%")

        chart = pd.DataFrame({
            "Delay Probability":[delay,100-delay]
        },index=["Delay","On Time"])

        st.bar_chart(chart)import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Flight Delay Prediction", page_icon="✈️")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1504196606672-aef5c9cefc92");
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Login system
users = {
    "admin":"flight123",
    "pilot":"sky456",
    "control":"tower789"
}

if "login" not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    st.title("✈ Flight Delay Prediction System")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]==password:
            st.session_state.login=True
            st.success("Login Successful")
        else:
            st.error("Invalid Login")

else:

    st.title("✈ Flight Delay Predictor")

    airport = st.selectbox(
        "Select Airport",
        ["Chennai","Delhi","Mumbai","Bangalore","Hyderabad"]
    )

    airline = st.selectbox(
        "Select Airline",
        ["IndiGo","Air India","SpiceJet","Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear","Rain","Storm","Fog"]
    )

    departure = st.slider("Departure Time",0,23)

    if st.button("Predict Delay"):

        delay = random.randint(0,100)

        st.subheader("Prediction Result")

        if delay > 60:
            st.error(f"⚠ High Delay Chance: {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay Chance: {delay}%")
        else:
            st.success(f"Low Delay Chance: {delay}%")

        chart = pd.DataFrame({
            "Delay Probability":[delay,100-delay]
        },index=["Delay","On Time"])

        st.bar_chart(chart)