import streamlit as st
import time

class AiModel:
    def __init__(self):
        time.sleep(5)  # Simulate heavy initialization
        self.model = "model"

    def predict(self, input):
        return "Prediction"
    
@st.cache_resource(show_spinner="Loading AI Model...", ttl=3600)
def load_ai_model():
    model = AiModel()
    return model

model = load_ai_model()
if model:
    st.write("AI Model Loaded Successfully!")

st.button("Reload Page")