import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

# Model and class mapping
import gdown
MODEL_PATH = "plant_species_Model_kaggle.h5"
GDRIVE_URL = "https://drive.google.com/uc?id=115K_QMpftnQxZ3DwoUargZp5WkOvGXcA"
CLASS_MAPPING = {
    'Amla': 0, 'Arali': 1, 'Ashoka': 2, 'Ashwagandha': 3, 'Avacado': 4,
    'Bamboo': 5, 'Basale': 6, 'Castor': 7, 'Corn': 8, 'Curry_Leaf': 9,
    'Doddapatre': 10, 'Ganike': 11, 'Guava': 12, 'Henna': 13, 'Mint': 14,
    'Nooni': 15, 'Pappaya': 16, 'Rose': 17, 'Wood_sorel': 18,
    'aloevera': 19, 'banana': 20, 'mango': 21, 'orange': 22, 'watermelon': 23
}
INDEX_TO_CLASS = {v: k for k, v in CLASS_MAPPING.items()}

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model..."):
            gdown.download(GDRIVE_URL, MODEL_PATH, quiet=False)
    model = tf.keras.models.load_model(MODEL_PATH)
    return model

def preprocess_image(image: Image.Image) -> np.ndarray:
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image = image.resize((224, 224))
    image_array = np.array(image).astype('float32') / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

st.title("🌿 Plant Species Classifier")
st.write("Upload a plant image to identify its species.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("")
        model = load_model()
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image, verbose=0)
        predicted_class_index = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][predicted_class_index])
        st.success(f"Prediction: {INDEX_TO_CLASS.get(predicted_class_index, 'Unknown')}")
        st.info(f"Confidence: {confidence:.2%}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
