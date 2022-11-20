# Cohere's imports
import cohere as co
from cohere.classify import Example
from conversant.prompt_chatbot import PromptChatbot
from conversant.utils import demo_utils

# Sreamlit
import streamlit as st
from streamlit_chat import message

# general imports
import ast
import copy
import os
import sys
import emoji

os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ["COHERE_API"]

co = co.Client(COHERE_API)

#------------------------------------------------------------
USER_AVATAR_SHORTCODE = ":bust_in_silhouette:"

def get_text():
    input_text = st.text_input("You: ","Hello, how are you?", key="input")
    return input_text 

def get_reply() -> None:
    """Replies query from the message input, and resets the message input"""
    _ = st.session_state.bot.reply(query=st.session_state.message_input)
    st.session_state.message_input = ""

def update_session_with_prompt() -> None:
    """Saves the prompt config dictionary into the session state."""
    if "bot" in st.session_state and st.session_state.bot:
        st.session_state.snapshot_prompt_config = copy.deepcopy(
            st.session_state.bot.prompt.to_dict()
        )
        st.session_state.snapshot_chatbot_config = copy.deepcopy(
            st.session_state.bot.chatbot_config
        )
        st.session_state.snapshot_client_config = copy.deepcopy(
            st.session_state.bot.client_config
        )

def initialize_chatbot() -> None:
    """Initializes the chatbot from a selected persona and saves the session state."""
    if st.session_state.persona.startswith("(launched)") and len(sys.argv) > 1:
        st.session_state.bot = demo_utils.decode_chatbot(
            sys.argv[1], client=co.Client(os.environ.get("COHERE_API"))
        )  # Launched via demo_utils.launch_streamlit() utility function
    elif st.session_state.persona == "":
        st.session_state.bot = None
    else:
        st.session_state.bot = PromptChatbot.from_persona(
            emoji.replace_emoji(st.session_state.persona, "").strip(),
            client=co.Client(os.environ.get("COHERE_API")),
        )
    if "bot" in st.session_state and st.session_state.bot:
        update_session_with_prompt()
    # Reset the edit_promp_json session state so we don't remain on the JSON editor when
    # changing to another bot. This is because st_ace is unable to write
    # new values from the current session state.
    st.session_state.edit_prompt_json = False
    
#---------------------------------------------------------------

st.title("Health-E: AI healthcare assistant")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


first_message = st.text_input("How may I help you today?", key="input_prompt")

health_e = PromptChatbot.from_persona("health-e", client=co)

st.write(health_e.reply(first_message))

message("My message") 
message("Hello bot!", is_user=True)













































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