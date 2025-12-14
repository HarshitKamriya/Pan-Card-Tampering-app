import os
import numpy as np
from skimage.metrics import structural_similarity
import imutils
import cv2
import streamlit as st
from PIL import Image

st.title("PAN Card Tampering Detection")
st.header("Enter image you want to detect")

uploaded_file = st.file_uploader("Upload image here", type=["jpg","jpeg","png"])
if uploaded_file is not None:
    # Convert uploaded file to NumPy array
    uploaded_img = np.array(Image.open(uploaded_file).resize((250,160)))
    original_img = cv2.imread("original.jpg")

    # Convert to grayscale
    original_gray = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    uploaded_gray = cv2.cvtColor(uploaded_img, cv2.COLOR_BGR2GRAY)

    # Structural similarity
    (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
    diff = (diff * 255).astype("uint8")

    # Threshold + contours
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # Draw contours
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(original_img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(uploaded_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Layout
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_img, caption="Original Image")
    with col2:
        st.image(uploaded_img, caption="Uploaded Image")

    col3, col4 = st.columns(2)
    with col3:
        st.image(diff, caption="Difference Image")
    with col4:
        st.image(thresh, caption="Threshold Image", clamp=True)

    # Decision logic (use thresh directly)
    non_zero_count = cv2.countNonZero(thresh)
    if non_zero_count > 500:
        st.error("⚠️ The image appears to be TEMPERED!")
    else:
        st.success("✅ The image appears to be NOT TEMPERED.")