import streamlit as st
from PIL import Image


with st.expander("Start Camera"):
    # Start the camera
    photo_img = st.camera_input("Camera")
    #print(photo_img)

if photo_img:
    #Create a pillow image instance
    img = Image.open(photo_img)

    #Convert a pillow image to grayscale
    gray_img = img.convert("L")

    #Render the grayscale image on the webpage
    st.image(gray_img)

