import datetime
import os
import streamlit as st
import requests
# import streamlit_scrollable_textbox as stx


year = datetime.datetime.now().year

st.set_page_config(page_title='Identity  Console',
                   page_icon='🏛️',
                   layout='centered',
)

hide_streamlit_style = '''
<style>
    header[data-testid="stHeader"] {
        opacity: 0.5;
    }
     iframe {
        border: 1px solid #dddddd;
        border-radius: 0.5rem;
    }
    div[data-testid="InputInstructions"] {
        visibility: hidden;
    }
</style>
'''

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
Backend_URL =os.environ["SERVER_URL"] if(os.environ["SERVER_URL"]) else "http://localhost:8000/" 
# Backend_URL = "http://localhost:8000/"

# UI
st.title(
    'Identity Console',
    anchor=False)
st.write(
    'Reconcillation API to find the Doc in Grandiose project'
)

st.text("You are pinging to /api/identity Endpoint")

email_input = st.text_input('Email', placeholder='akarshtripathi.work@gmail.com')
phone_number_input = st.text_input('Phone Number', placeholder='9971234477')
st.text("Before Querying, Run the Server")

col1, col2 = st.columns([1,1])
with col1:
    
    st.link_button("Run the Server First", Backend_URL)

with col2:
    button = st.button("Get Current DB State")
    if button:
        currentDatabaseState = requests.get(Backend_URL + "api/test/getAllData/").json()
        st.write("Current Database State")
        with st.container(height=500):
            st.write(currentDatabaseState)



query = st.button('Query', type='primary', use_container_width=True)

if query:
    data= {
        "email": email_input,
        "phonenumber": phone_number_input
    }
    print(data)
    response = requests.post(Backend_URL + "api/identity/", json=data, headers={'Content-Type': 'application/json'})
    with st.container(border=True):
        st.write("Response: ")
        st.write(response.json())
        st.write("Reload the database to see changes")



st.write("Created by - Akarsh Tripathi (akarshtripathi.work@gmail.com)")