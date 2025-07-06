from img_classification import teachable_machine_classification
import streamlit as st
from PIL import Image, ImageOps

st.header('Plantania')
st.write("Leaf disease detection")
uploaded_file = st.file_uploader("Choose plant image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Photo', use_column_width=True)
    st.write("")
    st.write("Detecting...")
    label = teachable_machine_classification(image, 'keras_model.h5')
    if label == 0:
        st.write("Cercospora leaf spot Gray leaf spot")
        
    if label == 1:
        st.write("Cherry Powdery_mildew")
        
    if label == 2:
        st.write("Cherry healthy")
        
    if label == 3:
        st.write("Apple healthy")
        
    if label == 4:
        st.write("Cedar apple rust")
        
    if label == 5:
        st.write("Apple Black rot")
        
    if label == 6:
        st.write("Apple scab")
    
