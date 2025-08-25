import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import json
from wordcloud import WordCloud

# ---- Load JSON ----
with open("mock_reviews.json", "r") as f:
    mock_data = json.load(f)

# Your JSON has {"reviews": [ ... ]}
df = pd.DataFrame(mock_data["reviews"])

st.title("Flex Living Reviews Dashboard")

# Show some data first
st.subheader("Sample Reviews Data")
st.write(df.head())

# ---- Recurring Issues Detection ----
st.subheader("Recurring Issues (Negative Reviews)")

# Filter only reviews with rating <= 3
negative_reviews = df[df["rating"] <= 3]["review_text"]

if not negative_reviews.empty:
    # Combine text
    text = " ".join(negative_reviews.tolist())

    # Cleanup
    text = re.sub(r"[^A-Za-z\s]", "", text)

    # Generate wordcloud
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

    # Show in Streamlit
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)
else:
    st.info("No negative reviews found 🚀")
