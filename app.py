import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model('./my_vgg16_model.h5')

# Define the preprocessing function for images
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    image = (image - mean) / std
    image = np.expand_dims(image, axis=0)
    return image

class_names = [
    'No DR',
    'Mild DR',
    'Moderate DR',
    'Severe DR',
    'Proliferative DR'
]

st.title("Diabetic Retinopathy Classification")
st.write("Upload an image to classify its diabetic retinopathy level.")

uploaded_file = st.file_uploader("Choose an image...", type="jpeg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    preprocessed_image = preprocess_image(image)
    predictions = model.predict(preprocessed_image)
    predicted_class = np.argmax(predictions, axis=1)[0]
    predicted_label = class_names[predicted_class]
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write(f"Prediction: {predicted_label}")
    st.write(f"Confidence: {np.max(predictions):.2f}")
