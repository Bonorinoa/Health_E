# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant import PromptChatbot
from conversant.prompts import ChatPrompt

# Sreamlit
import streamlit as st

import os

os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ["COHERE_API"]

co = co.Client(COHERE_API)

# Let's let the user pick from the default persona

st.title("Health-E: AI healthcare assistant")

first_message = st.text_input("How may I help you today?", key="input_prompt")

health_e = PromptChatbot.from_persona("health-e", client=co)

st.write(health_e.reply(first_message))













































# # Cohere's imports
# import cohere as co
# from cohere.classify import Example
# from conversant import PromptChatbot
# from conversant.prompts import ChatPrompt

# # Sreamlit
# import streamlit as st

# # General imports
# import pandas as pd
# import textwrap
# import numpy as np
# import json

# import os

# os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

# COHERE_API = os.environ["COHERE_API"]

# co = co.Client(COHERE_API)

# # Let's let the user pick from the default persona

# st.title("Health-E AI bot")