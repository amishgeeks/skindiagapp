import streamlit as st
import tensorflow as tf
import numpy as np

# Load your trained CNN model
model = tf.keras.models.load_model('path/to/your/model.h5')

# Function to make predictions
def predict_skin_condition(image):
    image = tf.image.resize(image, (150, 150)) # Resize to the input shape of your model
    image = image / 255.0  # Normalize the image
    image = np.expand_dims(image, axis=0)
    predictions = model.predict(image)
    return np.argmax(predictions, axis=1)  # Assuming the model outputs class probabilities

# Initialize user history
if 'user_history' not in st.session_state:
    st.session_state.user_history = []

# Streamlit app
st.title('Skin Condition Diagnosis App')

# Image upload widget
uploaded_file = st.file_uploader("Upload an image of your skin condition", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # Read the image
    image = tf.io.decode_image(uploaded_file.read(), channels=3)
    # Make a prediction
    condition = predict_skin_condition(image)
    # Update user history
    st.session_state.user_history.append(condition)
    # Display results
    st.write(f'Predicted skin condition: {condition}')

# Product recommendations based on the predicted condition
if condition == 0:
    st.write("Recommended product: Hydrating Moisturizer")
elif condition == 1:
    st.write("Recommended product: Acne Treatment Gel")
# Add more conditions and recommendations as necessary

# Display user history
st.write("Your history of diagnosed conditions:")
for idx, cond in enumerate(st.session_state.user_history):
    st.write(f"Diagnosis {idx + 1}: {cond}")