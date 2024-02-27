import utils
import streamlit as st
from io import StringIO

# Set the app title 
st.image("theplant-logo.png")
st.title('Text Preprocessing') 

tab1, tab2 = st.tabs(["Explore", "Clean file"])

with tab1:

    # Add a welcome message 
    st.write('Explore essential text preprocessing steps in Natural Language Processing') 

    # Create a text input 
    text_in = st.text_area('Enter text to be Preprocessed:', 'The European Parliament has played an active and important role.')

    # Define variable for text_out
    text_out = text_in

    # Multi select box
    preprocessing_1 = st.multiselect(
        "Select preprocessing steps: ",
        ['Tokenize', 'Remove stopwords', 'Remove punctuation', 'Lemmatize', 'Create bigrams', 'Nouns only'],
        default = 'Tokenize',
        key = 'tab1'
        )

    if 'Tokenize' in preprocessing_1:
        text_out = utils.tokenize(text_in)

    if 'Remove punctuation' in preprocessing_1:
        text_out = utils.remove_punctuation(text_out)

    if 'Remove stopwords' in preprocessing_1:
        text_out = utils.remove_stopwords(text_out)

    if 'Create bigrams' in preprocessing_1:
        text_out = utils.create_bigrams(text_out)

    if 'Lemmatize' in preprocessing_1:
        text_out = utils.lemmatize(text_out)

    if 'Nouns only' in preprocessing_1:
        text_out = utils.noun_only(text_out)

    # Create a text output
    st.text_area("Preprocessed text", text_out)

with tab2:
    # Add a welcome message 
    st.write('Explore essential text preprocessing steps in Natural Language Processing')

    # File upload control
    uploaded_file = st.file_uploader("Choose a file to be cleaned")
    if uploaded_file is not None:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        file_out = utils.tokenize(stringio.read())

    # Multi select box
    preprocessing_2 = st.multiselect(
        "Select preprocessing steps: ",
        ['Tokenize', 'Remove stopwords', 'Remove punctuation', 'Lemmatize', 'Create bigrams', 'Nouns only'],
        default = 'Tokenize',
        key = 'tab2'
        )

    if 'Remove punctuation' in preprocessing_2:
        file_out = utils.remove_punctuation(file_out)

    if 'Remove stopwords' in preprocessing_2:
        file_out = utils.remove_stopwords(file_out)

    if 'Create bigrams' in preprocessing_2:
        file_out = utils.create_bigrams(file_out)

    if 'Lemmatize' in preprocessing_2:
        file_out = utils.lemmatize(file_out)

    if 'Nouns only' in preprocessing_2:
        file_out = utils.noun_only(file_out)

    # Clean file
    if st.button('Clean file'):
        file_out = " ".join(file_out)
        st.download_button("Download cleaned file", file_out, file_name = "_".join(['cleaned', uploaded_file.name]))


