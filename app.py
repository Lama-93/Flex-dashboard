import streamlit as st
import json

st.title("Manager Dashboard")

# Load reviews
with open("mock_reviews.json", "r") as f:
    data = json.load(f)

reviews = data.get("reviews", [])

# Debug: print raw data
st.subheader("Raw Data Preview")
st.json(reviews)

# Show reviews in table
if reviews:
    st.subheader("Reviews Table")
    st.write(reviews)
else:
    st.warning("No reviews found in mock_reviews.json")
