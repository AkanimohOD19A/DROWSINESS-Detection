import torch
from PIL import Image
import streamlit as st
import numpy as np
import io
import os

## LOAD MODEL
run_model_path = './last_drowsy_v4.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=run_model_path)
## Placed Image
DEMO_IMAGE = './content/demo.jpg'


## Function
def save_predictedfile(uploadedfile):
    with open(os.path.join("./content/", "drowsiness-detection.jpg"), "wb") as f:
        f.write(uploadedfile)

def predict_img(img):
    image = np.array(Image.open(img))

    result = model(image)

    output = io.BytesIO()
    out_image = np.squeeze(result.render())
    output_img = Image.fromarray(out_image)
    output_img.save(output, format='JPEG')
    result_img = output.getvalue()

    save_predictedfile(result_img)

    return st.image(result_img)

st.sidebar.write(
    """
        Some Short Text Description about the Application Mode
    """
)
#
if st.sidebar.button("Use your Selfie"):
    SELFIE_IMAGE = "./content/selfie.jpg"
    DEMO_IMAGE = SELFIE_IMAGE
    predict_img(DEMO_IMAGE)

# if st.sidebar.button("Use your own image"):
img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
if img_file_buffer:
    UPLOADED_IMAGE = img_file_buffer
    DEMO_IMAGE = UPLOADED_IMAGE
    predict_img(UPLOADED_IMAGE)

    ## Save Result
    result_img = "./content/drowsiness-detection.jpg"
    with open(result_img, "rb") as file:
        btn = st.download_button(
            label="Save",
            data=file,
            file_name="drowsiness-detection.jpg",
            mime="image/jpeg")
# else:
#     predict_img(DEMO_IMAGE)

## Place Demo
st.sidebar.text("Placed Image")
st.sidebar.image(DEMO_IMAGE)
