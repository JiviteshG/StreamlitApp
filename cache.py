import streamlit as st
import requests
import time

@st.cache_data
def fetch_data(api_url):
    response = requests.get(api_url)
    time.sleep(1)  # Simulate network delay
    return response.json()

data = fetch_data("https://dog.ceo/api/breeds/image/random")
st.write(data)

st.image(data['message'], caption='Random Dog Image')

st.button("Reload Page")