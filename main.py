import streamlit as st
from PIL import Image
from backend import describe_human

st.title("Prends une photo en haute qualité")

uploaded_file = st.file_uploader(
    "Prends ou choisis une photo", 
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    human_description = describe_human(image)
    st.image(image, caption="Image importée", use_column_width=True)
    st.write(human_description)
