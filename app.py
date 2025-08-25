from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import streamlit as st
import pandas as pd
import json

# ---- Load mock reviews JSON file ----
try:
    with open("mock_reviews.json") as f:
        mock_data = json.load(f)
except Exception as e:
    st.error(f"Error loading JSON file: {e}")
    st.stop()

# ---- Convert JSON to DataFrame ----
df = pd.DataFrame(mock_data)

st.title("Flex Living Reviews Dashboard")

# ---- Show first rows for debugging ----
st.subheader("📊 Raw Data Preview")
st.write(df.head())

# ---- Recurring Issues Detection ----
st.subheader("Recurring Issues (Negative Reviews)")

# Filter only reviews with rating <= 3 (negative/neutral)
if "rating" in df.columns and "review_text" in df.columns:
    negative_reviews = df[df["rating"] <= 3]["review_text"]

    if not negative_reviews.empty:
        # Combine all text
        text = " ".join(negative_reviews.tolist())

        # Basic cleanup
        text = re.sub(r"[^A-Za-z\s]", "", text)

        # Generate wordcloud
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

        # Display in Streamlit
        fig, ax = plt.subplots(figsize=(10,5))
        ax.imshow(wordcloud, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.info("No negative reviews found 🚀")
else:
    st.warning("JSON must contain 'rating' and 'review_text' fields.")
