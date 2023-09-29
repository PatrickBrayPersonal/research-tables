import streamlit as st
from openai_interface import get_paper_df

template = """
Paper: {doi}
Provide the following information ({columns}) from the paper.
Information in each column must be under 50 words.
Leave the cell blank if the result is unclear.
Format the output as a .yaml file

Example Ouput:
Year Published: 2002
Research Objective: Observe Hormonal Effects of Intermittent Fasting
Key Contribution: Increases in corticosterone levels were found


Output:
"""


# Taking a list of arXiv dois
doi_input = st.text_area(
    "Enter a list of arXiv dois (comma separated):",
    value="1608.04471, 1710.09829, 1412.6980, 1406.2661",
)
dois = [doi.strip() for doi in doi_input.split(",")]

# Taking a list of strings
column_input = st.text_area(
    "Enter list of desired columns (comma separated):",
    value="Year Published, Research Objective, Meaningful Contributions, Tools Used, Relevance to CV (1-5)",
)
columns = [string.strip() for string in column_input.split(",")]


df_list = []
# Submit button
if st.button("Submit"):
    df = get_paper_df(dois, columns, dummy=True)
    st.dataframe(df.T)
