import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Startup Profit Prediction App")

# Input fields
rd_spend = st.number_input("R&D Spend", min_value=0.0)
admin = st.number_input("Administration", min_value=0.0)
marketing = st.number_input("Marketing Spend", min_value=0.0)

if st.button("Predict"):
    try:
        input_data = np.array([[rd_spend, admin, marketing]])
        profit = model.predict(input_data)
        st.success(f"Predicted Profit: ₹{profit[0]:,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
