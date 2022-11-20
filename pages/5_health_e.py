# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant.prompt_chatbot import PromptChatbot
from conversant.utils import demo_utils
from qa.bot import GroundedQaBot

# Sreamlit
import streamlit as st
from streamlit_chat import message
import streamlit.components.v1 as components

# general imports
import ast
import copy
import os
import sys
import emoji
from typing import Literal, Optional, Union

os.environ["SERP_API"] = "d795ad9b9ae5bac9213f4497cc5b1a0102281c2104b895ad908eb14452a295f9"
os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ['COHERE_API']
SERP_API = os.environ['SERP_API']

co = co.Client(COHERE_API)

bot = GroundedQaBot(COHERE_API, SERP_API)

#------------------------------------------------------------
COMPONENT_NAME = "streamlit_chat"

root_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(root_dir, "frontend/build")

_streamlit_chat = components.declare_component(
    COMPONENT_NAME,
    path = build_dir)

USER_AVATAR_SHORTCODE = ":bust_in_silhouette:"

# data type for avatar style
AvatarStyle = Literal[ 
    "adventurer", 
    "adventurer-neutral", 
    "avataaars",
    "big-ears",
    "big-ears-neutral",
    "big-smile",
    "bottts", 
    "croodles",
    "croodles-neutral",
    "female",
    "gridy",
    "human",
    "identicon",
    "initials",
    "jdenticon",
    "male",
    "micah",
    "miniavs",
    "pixel-art",
    "pixel-art-neutral",
    "personas",
]

def query_healthe(text_input):
    
	diagnose = health_e.reply(text_input)
 
	return diagnose

def query_qa(question):
    
    answer = bot.answer(question)
    
    return answer

def get_text():
    input_text = st.text_input("Hello! How may I assist you?", "", key="input_text")
    return input_text 

def chat_message(message: str,
                 is_user: bool = False,
                 avatar_style: Optional[AvatarStyle] = None,
                 seed: Optional[Union[int, str]] = 42,
                 key: Optional[str] = None):
    
    if not avatar_style:
        avatar_style = "pixel-art-neutral" if is_user else "bottts"

    _streamlit_chat(message=message, seed=seed, isUser=is_user, avatarStyle=avatar_style, key=key)
#---------------------------------------------------------------

st.title("Health-E: AI healthcare assistant")

health_e = PromptChatbot.from_persona("health-e", client=co)

if 'bot_output' not in st.session_state:
    st.session_state['bot_output'] = []

if 'user_text' not in st.session_state:
    st.session_state['user_text'] = []
    
if "bot" not in st.session_state:
    st.session_state['bot'] = health_e

user_input = get_text()

if user_input:
    st.session_state.user_text.append(user_input)
    output = query_healthe(user_input)
    st.session_state.bot_output.append(output)

if (st.session_state['bot_output']):

    for i in range(len(st.session_state['bot_output'])-1, -1, -1):
        chat_message(st.session_state['user_text'][i], is_user=True, key=str(i) + '_user')
        chat_message(st.session_state["bot_output"][i], key=str(i), avatar_style="gridy")
        












































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