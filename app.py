from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import streamlit as st
import pandas as pd
import json

# Load mock reviews JSON file
with open("mock_reviews.json") as f:
    mock_data = json.load(f)

# Convert JSON to DataFrame
df = pd.DataFrame(mock_data["reviews"])

st.title("Flex Living Reviews Dashboard")

# Display data for debugging
st.write(df.head())

# ---- Recurring Issues Detection ----
st.subheader("Recurring Issues (Negative Reviews)")

# Filter only reviews with rating <= 3 (likely negative/neutral)
negative_reviews = df[df["rating"] <= 3]["review_text"]

if not negative_reviews.empty:
    # Combine all text
    text = " ".join(negative_reviews.tolist())

    # Basic cleanup (remove punctuation/numbers)
    text = re.sub(r"[^A-Za-z\s]", "", text)

    # Generate wordcloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Display in Streamlit
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No negative reviews found in the current selection 🚀")
