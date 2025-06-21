import streamlit as st

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Startup profit Prediction App")

# Example input fields
feature1 = st.number_input("R&D Spend")
feature2 = st.number_input("Administration")
feature3 = st.number_input("Marketing Spend")

if st.button("Predict"):
    input_data = [[feature1, feature2, feature3]]
    prediction = model.predict(input_data)
    st.success(f"Prediction: {prediction[0]}")
