# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant.prompt_chatbot import PromptChatbot
import numpy as np

# Language Pipeline
from langchain.prompts import PromptTemplate
from langchain.llms import Cohere
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.utilities import SerpAPIWrapper

COHERE_API = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"
SERP_API = "da9cfc86b50b71d5c9a4b99bc809431337d1ad4d957992ddfd2aa2878ff719ac"
co = co.Client(COHERE_API)

search = SerpAPIWrapper(serpapi_api_key=SERP_API)

#qa_bot = GroundedQaBot(COHERE_API, SERP_API)
qa_model = Cohere(model="medium", cohere_api_key=COHERE_API)
chain = load_qa_with_sources_chain(qa_model, chain_type="stuff")

health_e = PromptChatbot.from_persona("health-e", client=co)


print(search.run("what is the best hospital in the world?"))