# Cohere's imports
import cohere as co
from cohere.classify import Example
from qa.bot import GroundedQaBot

# Sreamlit
import streamlit as st

# General imports
import pandas as pd
import textwrap
import numpy as np
import json

import os

# Serp API key
# https://serpapi.com/manage-api-key
#serp_key = "99bdacc49c981c56debcd24eb068f5eebed6a273e37c1410584599a6fbf4155c"

os.environ["SERP_API"] = "99bdacc49c981c56debcd24eb068f5eebed6a273e37c1410584599a6fbf4155c"
os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ['COHERE_API']
SERP_API = os.environ['SERP_API']

#--------------------------------------------------

def wake_up_bot(question):
  '''
  Call bot and google possible answers to the given question
  Inputs:
    question(str): The question to answer
  Returns:
    answer
  '''
  # Set up QA Bot
  bot = GroundedQaBot(COHERE_API, SERP_API)
  
  answer = bot.answer(question)
  
  return answer

#----------------------------------------------------

form = st.form(key="user_settings")
with form:
  st.write("Ask me anything")
  # User input - Industry name
  question = st.text_input("Question", key = "question")

  # Submit button to start generating ideas
  generate_button = form.form_submit_button("Ask.")
  if generate_button:
    if question == "":
      st.error("Sure you don't wan't to ask anything?")
    else:
      my_bar = st.progress(0.05)
      st.subheader("Answers:")
      
      answers = wake_up_bot(question)
      
      st.write(answers)