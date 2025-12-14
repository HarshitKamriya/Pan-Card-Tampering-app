# PAN Card Tampering Detection 🪪🔍

A simple **Streamlit web app** that detects whether a PAN card image has been tampered with by comparing it against an original reference image.  
It uses **OpenCV**, **scikit-image**, and **imutils** to compute structural similarity, highlight differences, and display a verdict.

---

## 🚀 Features
- Upload a PAN card image via the Streamlit interface.
- Compare against a stored original image (`original.jpg`).
- Convert both images to grayscale for analysis.
- Compute **Structural Similarity Index (SSIM)** to detect differences.
- Highlight tampered regions with bounding boxes.
- Display:
  - Original image
  - Uploaded image
- Verdict: **Tempered** ⚠️ or **Not Tempered** ✅

---


