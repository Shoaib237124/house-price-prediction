import streamlit as st
import pickle
import json
import numpy as np

# Load model and columns
with open("house_price_model.pickle", "rb") as f:
    model = pickle.load(f)

with open("columns.json", "r") as f:
    data_columns = json.load(f)['data_columns']   # expecting { "data_columns": [...] }

# Extract location names (all columns after sqft, bath, bhk)
locations = data_columns[3:]

# Prediction function
def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(model.predict([x])[0], 2)

# Streamlit UI
st.set_page_config(page_title="🏠 House Price Predictor", layout="centered")

st.title("🏠 Bengaluru House Price Prediction App")
st.write("Enter details below to estimate house price:")

sqft = st.number_input("Total Square Feet", min_value=200, max_value=10000, step=50)
bhk = st.number_input("Number of BHK", min_value=1, max_value=10, step=1)
bath = st.number_input("Number of Bathrooms", min_value=1, max_value=10, step=1)
location = st.selectbox("Location", sorted(locations))

if st.button("Predict Price"):
    # Basic validation
    if sqft < bhk * 300:
        st.error("❌ Invalid input: Too small area for given BHK.")
    elif bath > bhk + 2:
        st.error("❌ Invalid input: Too many bathrooms for given BHK.")
    else:
        price = predict_price(location, sqft, bath, bhk)
        price = max(0, price)
        st.success(f"Estimated Price: ₹ {price} Lakhs")
