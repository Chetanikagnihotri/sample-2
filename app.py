import streamlit as st
import cv2
import numpy as np

st.title("Webcam Live Feed")
st.write("This application shows the live feed from your webcam using OpenCV and Streamlit.")

# Start video capture from webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    st.error("Error: Could not open webcam.")
else:
    # Create a placeholder for the video frame
    frame_placeholder = st.empty()

    # Loop to continuously get frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Could not read frame from webcam.")
            break
        
        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in the Streamlit app
        frame_placeholder.image(frame, channels="RGB")
        
        # Add a small delay to the loop
        cv2.waitKey(1)

# Release the webcam when done
cap.release()
