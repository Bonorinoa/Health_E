## First window to show. This is the main page of the web application.
import streamlit as st
import pandas as pd
import numpy as np
import json

import os
 
os.environ["COHERE_API"] = "mhsnOPXxi1m91vlrQJ6VsKFoDVhiqlKPeYHtEsZV"

COHERE_API = os.environ['COHERE_API']

st.caption("Replacing paperwork with AI ")
st.title("HEALth-E :blue_heart:")
st.markdown("In hospitals paperwork takes alot of time from the patients and doctors. Health-e eliminate the managerial paperwork and make things smoother for the patients. Our bot helps the user finding best solutions for their problem with just one line prompts.")

from PIL import Image
image = Image.open('healthe.png')

st.image(image)

st.write('')

st.write("With just one prompt the users are connected with the required doctor and making appointments becomes super easy.")
st.write("Additionally, our bot shares useful online resources.")
st.write(''
         '')
st.subheader('This is our workflow')
from PIL import Image
image = Image.open('workflow.png')

st.image(image, caption='workflow')
