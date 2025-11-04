import streamlit as st

def text_analyzer(text):
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    vowels = "aeiouAEIOU"
    vowels_count = sum(1 for ch in text if ch in vowels)
    
    return num_words, num_chars, vowels_count


# Streamlit UI
st.title("🧠 Text Analyzer App")

st.write("Enter a sentence below to analyze the text:")

# Text input area
sentence = st.text_area("Enter your sentence:")

# Analyze button
if st.button("Analyze"):
    if sentence.strip() == "":
        st.warning("⚠️ Please enter some text to analyze.")
    else:
        num_words, num_chars, vowels_count = text_analyzer(sentence)

        # Display results
        st.success("✅ Analysis Complete!")
        st.write(f"**Number of words:** {num_words}")
        st.write(f"**Number of characters:** {num_chars}")
        st.write(f"**Number of vowels:** {vowels_count}")
