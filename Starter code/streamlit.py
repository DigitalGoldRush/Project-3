import streamlit as st
from PIL import Image

st.markdown("PLaying Card Tester")
st.text(" \n")

image = Image.open('Js.png')
#image = image.resize((30, 40))
st.image(image, caption='Nine of diamonds in Streamlit')
