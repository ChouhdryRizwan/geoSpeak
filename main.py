import streamlit as st
from utility import load_languages, generate_translation

# Configure Streamlit page settings
st.set_page_config(
    page_title="Geo-Speak Translate!",
    page_icon=":earth_americas:",  # Favicon emoji for translation
    layout="centered",
)

# Load languages from the JSON file
languages = load_languages('src/languages.json')  # Replace with the actual path to your JSON file

# Initialize translation history in Streamlit if not already present
if "translation_history" not in st.session_state:
    st.session_state.translation_history = []

# Display the translator's title on the page
st.title("🌍 Geo-Speak Translate")

# Language selection input box comes first
language = st.selectbox("Select target language", options=languages)

# Text input box for text to translate
if "source_text" not in st.session_state:
    st.session_state["source_text"] = ""

source_text = st.text_area("Enter text to translate:", value=st.session_state["source_text"], height=150)

# Add the translate button after input boxes
if st.button("Translate"):
    if source_text and language:
        # Use the utility function to get the translation
        translation_response = generate_translation(source_text, language)

        # Display the current translation result with light background
        st.markdown(f"<div style='background-color: #cff2c7; padding: 10px;'>{translation_response}</div>", unsafe_allow_html=True)

        # Save translation history
        st.session_state.translation_history.append(
            {"source": source_text, "target_language": language, "translation": translation_response}
        )

        # Clear the text input box after translation
        st.session_state["source_text"] = ""

# Divider between current translation and history
if st.session_state.translation_history:
    st.markdown("***")  # Horizontal line separator
    st.markdown("## Translation History")

    # Display the translation history
    for entry in st.session_state.translation_history:
        st.markdown(f"**Original ({entry['target_language']}):** {entry['source']}")
        st.markdown(f"<div style='background-color: #cff2c7;; padding: 10px;'>{entry['translation']}</div>", unsafe_allow_html=True)
        st.markdown("---")
