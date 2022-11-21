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
st.subheader('This is the conversation flow')
from PIL import Image
image = Image.open('health_e_flow.png')

st.image(image, caption='conversation flow')

st.subheader("Our Ideals")
st.write("")
st.write("This AI will help hospitals and Doctors skip the crucial paperwork needed before you get treatment from the doctor, making it possible for patients directly to get a bed when they enter the hospital. With Health-e we eliminate this paperwork. When there is a person in need of medical attention and no medical assistance on site, Health-e is always there to help with important information and simultaneously analyze the situation. Every second counts in these situations Health-e could be there in an instant with medical assistance in seconds. But it does not end there Health-e gives you many tips and tricks with even the trivial problems just in your pocket and one question away.")
