import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="AI Flight Delay System", page_icon="✈️", layout="centered")

# ---------- Background Image ----------
st.markdown("""
<style>

.stApp {
background-image: url("https://images.unsplash.com/photo-1436491865332-7a61a109cc05");
background-size: cover;
background-position: center;
}

.login-box {
background: rgba(0,0,0,0.75);
padding: 40px;
border-radius: 15px;
width: 350px;
margin:auto;
color:white;
}

.title {
text-align:center;
font-size:40px;
font-weight:bold;
color:white;
}

.subtitle {
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------- Users ----------
users = {
"admin":"flight123",
"pilot":"sky456",
"control":"tower789"
}

if "login" not in st.session_state:
    st.session_state.login = False


# ---------- LOGIN PAGE ----------
if not st.session_state.login:

    st.markdown('<div class="title">✈ AI Flight Delay System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Aviation Delay Prediction Dashboard</div>', unsafe_allow_html=True)

    st.markdown('<div class="login-box">', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]==password:
            st.session_state.login = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- MAIN DASHBOARD ----------
else:

    st.title("✈ Flight Delay Prediction Dashboard")

    st.write("Enter flight information to predict possible delay.")

    airport = st.selectbox(
        "Departure Airport",
        ["Chennai International Airport",
        "Delhi Airport",
        "Mumbai Airport",
        "Bangalore Airport",
        "Hyderabad Airport"]
    )

    airline = st.selectbox(
        "Airline",
        ["IndiGo","Air India","SpiceJet","Vistara"]
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Clear","Rain","Fog","Storm"]
    )

    departure = st.slider("Departure Hour",0,23)

    if st.button("Predict Flight Delay"):

        delay = random.randint(0,100)

        st.subheader("Prediction Result")

        if delay > 60:
            st.error(f"⚠ High Delay Probability : {delay}%")
        elif delay > 30:
            st.warning(f"Moderate Delay Probability : {delay}%")
        else:
            st.success(f"Low Delay Probability : {delay}%")

        chart = pd.DataFrame({
        "Status":["Delay","On Time"],
        "Percentage":[delay,100-delay]
        })

        st.bar_chart(chart.set_index("Status"))
