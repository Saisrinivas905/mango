# Download pre-trained emotion detection model
#!wget -q https://github.com/OlafenwaMoses/Emotion-Recognition/releases/download/v0.1/emotion_model.h5

import cv2
import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model

# Load pre-trained emotion detection model
emotion_model = load_model('emotion_model.hdf5')

# Define the list of emotions
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Function to detect emotion from the face
def detect_emotion(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    frame = cv2.resize(frame, (48, 48))  # Resize to fit the emotion detection model
    frame = np.expand_dims(frame, axis=0)
    frame = np.expand_dims(frame, axis=-1)
    emotion_prediction = emotion_model.predict(frame)
    dominant_emotion = emotion_labels[np.argmax(emotion_prediction)]
    return dominant_emotion

# Function to display emotions on the face
def display_emotion(frame):
    emotion = detect_emotion(frame)
    frame = cv2.putText(frame, emotion, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    return frame

# Interface
iface = gr.Interface(display_emotion, 
                     inputs="webcam", 
                     outputs="image",
                     title="Emotion Detection",
                     description="Detect the dominant emotion from your face.")
iface.launch(share=True)
