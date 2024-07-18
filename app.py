import streamlit as st
import cv2
import numpy as np
import time

def main():
    st.title("Webcam Live Feed")
    st.write("This application uses your webcam to display a real-time video feed.")

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    
    # Check if the webcam is opened correctly
    if not cap.isOpened():
        st.error("Unable to open webcam.")
        return
    
    # Placeholder for the video frame
    frame_placeholder = st.empty()

    # Main loop to display the video feed
    while True:
        # Read frame from the webcam
        ret, frame = cap.read()
        
        if not ret:
            st.error("Failed to read frame from webcam.")
            break
        
        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Display the frame in Streamlit
        frame_placeholder.image(frame_rgb, channels="RGB")
        
        # Add a short delay to make the video smoother
        time.sleep(0.03)
        
        # Break the loop if the user presses the "Stop" button
    
    
    # Release the webcam
    cap.release()

if __name__ == "__main__":
    main()
