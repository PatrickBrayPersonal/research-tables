import streamlit as st

import pandas as pd


import streamlit as st

# Taking a list of arXiv dois
dois = st.text_area("Enter a list of arXiv dois (separated by a comma):")
dois_list = [doi.strip() for doi in dois.split(',')]

# Taking a list of strings
strings = st.text_area("Enter a list of strings (separated by a comma):")
strings_list = [string.strip() for string in strings.split(',')]

# Submit button
if st.button('Submit'):
    st.write('Hello World')

