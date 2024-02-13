import json
import time
import requests

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/8a50ffe1-21f4-466b-828a-4d8380f19ae7/I8vj68E5IJ.json"
lottie_url_download = "https://lottie.host/290016a6-d650-4a32-85c7-4d77b0a892ca/4rNL8XZeZt.json"
lottie_hello = load_lottieurl(lottie_url_hello)
lottie_download = load_lottieurl(lottie_url_download)


st_lottie(lottie_hello, key="hello")

if st.button("Download"):
    with st_lottie_spinner(lottie_download, key="download"):
        time.sleep(5)
    st.balloons()