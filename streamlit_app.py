import streamlit as st
from PIL import Image

st.title("Signterpreter")
st.header("header")

filename = st.file.uploader("upload_file")
image = Image.open(filename)

#st.write(image)
st.selectbox("navigation", ("Demo1", "Demo2"))