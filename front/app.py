import streamlit as st
import requests
from st_pages import hide_pages, Page

# FastAPI base URL
base_url = "http://localhost:8000/jibi"  # Update with your actual URL

# Initialize session state
if 'user_token' not in st.session_state:
    st.session_state.user_token = None

# Streamlit App
st.title("Jibi")

# Sidebar Navigation
page = st.selectbox("Select Page", ["SignUp", "SignIn"])

if page == "SignUp":
    st.header("Signup")
    signup_email = st.text_input("Email")
    signup_username = st.text_input("Username")
    signup_password = st.text_input("Password", type="password", key="signup_password")
    if st.button("Sign Up"):
        signup_response = requests.post(f"{base_url}/signup/{signup_email}", params={"username": signup_username, "password": signup_password})
        if signup_response.status_code == 200:
            st.session_state.user_token = signup_response.json().get("user", {}).get("token")
            st.success("SignUp Successful!")
            hide_pages([Page("./app.py")])
        else:
            st.warning(signup_response.json().get('message', ''))

elif page == "SignIn":
    if 'user_token' not in st.session_state:
        st.session_state.user_token = None
    st.header("Sign In")
    signin_email = st.text_input("Email")
    signin_password = st.text_input("Password", type="password", key="signin_password")
    if st.button("Sign In"):
        signin_response = requests.post(f"{base_url}/signin/{signin_email}", params={"email": signin_email, "password": signin_password})
        print(signin_response.status_code)
        if signin_response.status_code == 200:
            # Sign-in successful, store the token in session state
            st.session_state.user_token = signin_response.json().get("user", {}).get("token")
            st.success("Signin Successful!")
            hide_pages([Page("./app.py")])
        else:
            st.warning(signin_response.json().get('message', ''))
