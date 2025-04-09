import streamlit as st
import pandas as pd
import textstat

st.set_page_config(page_title="Live Syllable Counter", layout="wide")

st.title("Live Syllable Counter")
st.markdown("Real-time syllable counting for English & Hebrew.")

# Live input box
user_input = st.text_area("Type your text here:", height=200)

# Split text into lines
lines = user_input.split("\n")

# Placeholder function for Hebrew syllables (until morphology lib works)
def count_hebrew_syllables(word):
    # VERY simple fallback: count vowel-like characters
    vowels = "אֱֲֳִֵֶַָֹֻּׂ"
    return sum(1 for char in word if char in vowels) or 1 if word else 0

data = []
for idx, line in enumerate(lines):
    line = line.strip()
    if not line:
        continue
    english_syllables = sum(textstat.syllable_count(word) for word in line.split())
    hebrew_syllables = sum(count_hebrew_syllables(word) for word in line.split())
    data.append({
        "Line": idx,
        "Text": line,
        "English Syllables": english_syllables,
        "Hebrew Syllables": hebrew_syllables
    })

# Display results
st.subheader("Syllables per Line")
df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)
