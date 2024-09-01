import cv2
import numpy as np
import streamlit as st
from PIL import Image

def enhance_greenery(image):
    # Convert the image from BGR to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Split the HSV image into three channels
    h, s, v = cv2.split(hsv_image)
    
    # Convert image from BGR to separate channels
    b, g, r = cv2.split(image)
    
    # Create a mask where green is dominant
    green_mask = (g > r) & (g > b)
    
    # Increase saturation only where the green mask is true
    s[green_mask] = s[green_mask] * 100
    
    # Clip the values to stay within the valid range [0, 255]
    s = np.clip(s, 0, 255).astype(np.uint8)
    
    # Merge the channels back
    enhanced_hsv_image = cv2.merge([h, s, v])
    
    # Convert the image back from HSV to BGR
    enhanced_image = cv2.cvtColor(enhanced_hsv_image, cv2.COLOR_HSV2BGR)
    
    return enhanced_image

# Streamlit App
st.title("Greenery Enhancer")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert the uploaded file to an OpenCV image
    image = Image.open(uploaded_file)
    image = np.array(image)
    original_image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    # Enhance the greenery in the image
    enhanced_image = enhance_greenery(original_image)
    
    # Convert BGR to RGB for displaying with Streamlit
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    enhanced_image_rgb = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
    
    # Display the original and enhanced images side by side
    st.subheader("Original Image")
    st.image(original_image_rgb, caption="Original Image", use_column_width=True)
    
    st.subheader("Greenery Enhanced Image")
    st.image(enhanced_image_rgb, caption="Greenery Enhanced Image", use_column_width=True)
