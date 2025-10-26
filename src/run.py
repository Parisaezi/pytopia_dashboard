import json
import streamlit as st
import numpy as np
import seaborn as sns 
from io import StringIO
import matplotlib.pyplot as plt
from PIL import Image

# Login
login_option = st.sidebar.radio("Login/Signup", ("Login", "Signup"))
if login_option == "login":
    with st.sidebar.form("Login"):
        st.write("Login Here")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Signup"):
        st.write("Signup Here")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        email = st.text_input("Email")
        
        submitted = st.form_submit_button("Login")
        if submitted:
            pass        

# Banner
banner = Image.open('/mnt/d/projects/git-practice/pytopia-dashboard/data/banner.jpg')
st.image(banner, width=1000)
st.title(':zap: Pytopia Dashboard')

# Metrics
col1, col2 = st.columns(2)
col1.metric(label="Pytopia Telegram Members", value="7000", delta="+100")
col2.metric(label="Pytopia Website Members", value="7000", delta="+100")

# Statistics
with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)
    
# User info
with st.expander("User Profile:"):
    col1, col2 = st.columns(2)
    col1.text_input("Name:")
    col2.text_input("Location:")
    st.camera_input("Camera Input:", key="camera_input")
    
    
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)
        
    data = json.loads(string_data)
    st.json(data['messages'][0])
