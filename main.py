import streamlit as st
from PIL import Image

st.title("Prendre une photo avec l'appareil photo")

# Composant pour capturer une image
photo = st.camera_input("Prenez une photo")

# Affichage ou traitement de la photo
if photo:
    image = Image.open(photo)
    st.image(image, caption="Voici votre photo", use_container_width=True)