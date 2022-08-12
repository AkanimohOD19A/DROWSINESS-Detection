import streamlit as st
from PIL import Image
import numpy as np
import torch
import io
import os

## Introduction
st.title("DROWSINESS DETECTION")
st.subheader("in still images")

## Application States
APPLICATION_MODE = st.sidebar.selectbox("Our Options",
                                        ["About the App", "Take a Selfie", "Predict", "Play Around"]
                                        )

## Placed Image
DEMO_IMAGE = './content/demo.jpg'

## Load Model
run_model_path = './last_drowsy_v4.pt'
model = torch.hub.load('ultralytics/yolov5', 'custom', path=run_model_path)
model.eval()

print("DONE LOADING MODEL")

## ImageSave Function
def save_uploadedfile(uploadedfile):
    with open(os.path.join("./content/", "selfie.jpg"), "wb") as f:
        f.write(uploadedfile.getbuffer())

def predict_img(img):
    image = np.array(Image.open(img))

    result = model(image)

    output = io.BytesIO()
    out_image = np.squeeze(result.render())
    output_img = Image.fromarray(out_image)
    output_img.save(output, format='JPEG')
    result_img = output.getvalue()
    return st.image(result_img)

if APPLICATION_MODE == "About the App":
    st.markdown("Some Long Text Description about the Application **Web Graphical User Interface**")
    st.markdown(
        """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
            width: 350px;
        }
        [data-testid="stSidebar"][aria-expanded="false] > div:first-child{
            width: 350px;
            margin-left: -350px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        #   About Me \n
            Hey this how to create a newline \n

            Test this and see \n
        """
    )

if APPLICATION_MODE == "Take a Selfie":
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
        if st.sidebar.button("Save Image"):
            ## Function to save image
            save_uploadedfile(picture)
            st.success("Saved File")
            st.sidebar.image("./content/selfie.jpg", caption="Selfie")

elif APPLICATION_MODE == "Predict":
    st.sidebar.write(
        """
            Some Short Text Description about the Application Mode
        """
    )

    if st.sidebar.button("Use your Selfie"):
        SELFIE_IMAGE = "./content/selfie.jpg"
        DEMO_IMAGE = SELFIE_IMAGE
        predict_img(DEMO_IMAGE)

    if st.sidebar.button("Use your own image"):
        img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
        if img_file_buffer is not None:
            image = np.array(Image.open(img_file_buffer))
            result = model(image)

            output = io.BytesIO()
            out_image = np.squeeze(result.render())
            output_img = Image.fromarray(out_image)
            output_img.save(output, format='JPEG')
            result_img = output.getvalue()
            st.image(result_img)

            ## Save Result
            btn = st.download_button(
                label="Keep a copy",
                data=result_img,
                file_name="meshed_image.png",
                mime="image/jpeg")
        else:
            predict_img(DEMO_IMAGE)

    ## Place Demo
    st.sidebar.text("Placed Image")
    st.sidebar.image(DEMO_IMAGE)

elif APPLICATION_MODE == "Play Around":
    st.sidebar.subheader("Let's take some interesting image augmentation techniques and apply them")

    if st.sidebar.button("Style A"):
        convert_img = Image.open(DEMO_IMAGE).convert('1')
        st.image(convert_img, caption="roughEntry|Just Don't Caught")

    ## Leave a sample down
    st.sidebar.image(DEMO_IMAGE)
