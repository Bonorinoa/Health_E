## First window to show. This is the main page of the web application.
import streamlit as st
import pandas as pd
import numpy as np
import json

import os
 
os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ['COHERE_API']

# Nested loop three levels deep

st.title('Welcome to the main page of the web application')