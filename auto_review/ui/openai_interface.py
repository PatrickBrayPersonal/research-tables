import json

import pandas as pd
import yaml
from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from loguru import logger

load_dotenv(find_dotenv())
DUMMY_FILENAME = "last_response.json"

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


llm = ChatOpenAI(temperature=0.1)
tools = load_tools(
    ["arxiv"],
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)


def get_paper_df(dois, columns, dummy=False):
    logger.info(f"Columns: {columns}")

    response_list = []
    if dummy:
        response_list = get_dummy_info()
    else:
        for doi in dois:
            logger.info(f"Doi: {doi}")
            response = get_paper_info(doi=doi, columns=columns)
            response_list.append(response)
            logger.info(f"Response: \n{response}")

    df_list = []
    for doi, response in zip(dois, response_list):
        try:
            response_dict = yaml.safe_load(response)
            response_dict["doi"] = doi
            response_dict = {k: [v] for k, v in response_dict.items()}
            df_list.append(pd.DataFrame(response_dict))
        except Exception as e:
            logger.error(f"Yaml converting error: {e}")

    df = pd.concat(df_list, ignore_index=True)
    df = df.set_index("doi")
    save_dummy_info(response_list)
    return df


def get_paper_info(**kwargs):
    prompt = PromptTemplate(
        input_variables=["columns", "doi"],
        template=template,
    )

    return agent_chain.run(prompt.format(**kwargs))


def save_dummy_info(response_list):
    with open(DUMMY_FILENAME, "w") as f:
        json.dump(response_list, f, indent=4)


def get_dummy_info(**kwargs):
    with open(DUMMY_FILENAME, "r") as f:
        return json.load(f)


if __name__ == "__main__":
    get_paper_df(dois=[2, 3, 3], columns=["a", "B"], dummy=True)
