from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import streamlit as st
import pandas as pd
import json

st.title("Flex Living Reviews Dashboard")

# ---- Load mock reviews JSON file ----
try:
    with open("mock_reviews.json") as f:
        mock_data = json.load(f)
    st.success("✅ JSON file loaded successfully")
except Exception as e:
    st.error(f"❌ Error loading JSON file: {e}")
    st.stop()

# ---- Convert JSON to DataFrame ----
if "reviews" in mock_data:
    df = pd.DataFrame(mock_data["reviews"])
    st.subheader("📊 Raw Data Preview")
    st.write(df.head())
else:
    st.error("❌ JSON does not contain 'reviews' key")
    st.stop()

# ---- Recurring Issues Detection ----
st.subheader("Recurring Issues (Negative Reviews)")

# Ensure required columns exist
if "rating" in df.columns and "review_text" in df.columns:
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
        st.info("No negative reviews found 🚀")
else:
    st.error("❌ DataFrame missing 'rating' or 'review_text' columns")
