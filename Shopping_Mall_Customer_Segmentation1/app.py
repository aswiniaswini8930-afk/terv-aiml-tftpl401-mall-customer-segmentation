
import streamlit as st
import pandas as pd
import joblib

# Load trained model and scaler
model = joblib.load("Shopping_Mall_Customer_Segmentation1/models/kmeans_model.pkl")
scaler = joblib.load("Shopping_Mall_Customer_Segmentation1/models/scaler.pkl")

st.set_page_config(
    page_title="Shopping Mall Customer Segmentation",
    page_icon="🛍️"
)

st.title("🛍️ Shopping Mall Customer Segmentation")
st.write("Predict a customer's shopping behaviour using K-Means clustering.")

st.subheader("Enter Customer Details")

age = st.number_input("Age", 18, 75, 30)
income = st.number_input("Annual Income (₹ Lakhs)", 2.0, 35.0, 8.0)
score = st.number_input("Spending Score", 1, 100, 60)
visits = st.number_input("Visits per Month", 0.0, 14.9, 5.0)
basket = st.number_input("Average Basket Value (₹)", 250.0, 7765.38, 2000.0)
tenure = st.number_input("Customer Tenure (Years)", 0.84, 5.84, 3.0)

if st.button("Predict Customer Segment"):

    monthly_spend = visits * basket

    customer = pd.DataFrame([[
        age,
        income,
        score,
        visits,
        monthly_spend,
        tenure
    ]], columns=[
        "age",
        "annual_income_lakh",
        "spending_score",
        "visits_per_month",
        "monthly_spend",
        "tenure_years"
    ])

    scaled_customer = scaler.transform(customer)
    cluster = int(model.predict(scaled_customer)[0])

    personas = {
        0: "Premium High-Value Customers",
        1: "Young Frequent Shoppers",
        2: "Budget-Conscious Occasional Shoppers"
    }

    recommendations = {
        0: "VIP rewards, premium launches and personalised experiences.",
        1: "Loyalty points, combo offers and cross-category promotions.",
        2: "Seasonal discounts, family packages and comeback offers."
    }

    st.success("Prediction completed!")

    st.subheader(f"Cluster {cluster}")
    st.write("**Customer Persona:**", personas[cluster])
    st.write("**Marketing Recommendation:**", recommendations[cluster])
    st.metric("Estimated Monthly Spending", f"₹{monthly_spend:,.2f}")
