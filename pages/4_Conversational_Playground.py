# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant import PromptChatbot

# Sreamlit
import streamlit as st

# General imports
import pandas as pd
import textwrap
import numpy as np
import json

import os

os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ["COHERE_API"]

co = co.Client(COHERE_API)

# Let's let the user pick from the default persona

st.title("Conversant AI bot")

persona = st.selectbox(
    'How would you like to be contacted?',
    ("fantasy-wizard", 
     "client-support", 
     "fortune-teller",
     "injured-person",
     "math-teacher",
     "personal-trainer"
     ))

st.write('You selected:', persona)

bot = PromptChatbot.from_persona(persona, client=co)

first_message = st.text_input("Start a chat", key="input_prompt")

st.write( bot.reply(first_message) )