import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
import pickle
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import json
import time
# Load environment variables from .env file
load_dotenv()
# Streamlit user interface
st.title('Crude Oil Dashboard: Welcome to GeopPetro, Your Price Prediction and Production Forecasting Application.')

# import streamlit as st
# import json

# st.title("Manager Dashboard")

# # Load reviews
# with open("mock_reviews.json", "r") as f:
#     data = json.load(f)

# reviews = data.get("reviews", [])

# # Debug: print raw data
# st.subheader("Raw Data Preview")
# st.json(reviews)

# # Show reviews in table
# if reviews:
#     st.subheader("Reviews Table")
#     st.write(reviews)
# else:
#     st.warning("No reviews found in mock_reviews.json")
