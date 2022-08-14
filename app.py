import streamlit as st
from PIL import Image
import numpy as np
import torch
import io
import os

## Introduction
st.title("DROWSINESS DETECTION")
st.subheader("An implementation of Machine Learning to determine when user"
             " might be feeling a little drowsy.")
st.markdown("---")

st.subheader("Powered by YOLOv5 and PyTorch! \n"
         "\n"
         "Author: **AfroLogicInsect**")

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
def save_predictedfile(uploadedfile):
    with open(os.path.join("./content/", "drowsiness-detection.jpg"), "wb") as f:
        f.write(uploadedfile)

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

    save_predictedfile(result_img)

    return st.image(result_img)

if APPLICATION_MODE == "About the App":
    st.markdown("**Web Graphical User Interface** \n"
                "Follow the side bar options, "
                "take a selfie with your device if you do not have an image to upload \n"
                "Predict, to test our predictions \n"
                "The last option is for some Image Augmentation.")
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
        Share your feedback with me - danielamahtoday@gmail.com
        """
    )

if APPLICATION_MODE == "Take a Selfie":
    picture = st.camera_input("Take a picture")

    if picture:
        st.sidebar.image(picture, caption="Selfie")
        if st.button("Save Image"):
            ## Function to save image
            save_uploadedfile(picture)
            st.sidebar.success("Saved File - Click to Download")
            selfie_img = "./content/selfie.jpg"
            with open(selfie_img, "rb") as file:
                btn = st.sidebar.download_button(
                    label="Download",
                    data=file,
                    file_name="selfie.jpg",
                    mime="image/jpeg")

    st.write("Click on **Clear photo** to retake picture")

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

    st.sidebar.write("**Use your own image**")
    img_file_buffer = st.sidebar.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if img_file_buffer is not None:
        UPLOADED_IMAGE = img_file_buffer
        DEMO_IMAGE = UPLOADED_IMAGE
        predict_img(UPLOADED_IMAGE)

        ## Save Result
        result_img = "./content/drowsiness-detection.jpg"
        with open(result_img, "rb") as file:
            btn = st.download_button(
                label="Save Result",
                data=file,
                file_name="drowsiness-detection.jpg",
                mime="image/jpeg")
    else:
        predict_img(DEMO_IMAGE)

    ## Place Demo
    st.sidebar.text("Placed Image")
    st.sidebar.image(DEMO_IMAGE)


elif APPLICATION_MODE == "Play Around":
    st.sidebar.subheader("Let's take some interesting image augmentation techniques and apply them")
    st.sidebar.markdown('---')

    img_file_buffer = st.sidebar.file_uploader("Try It!", type=["jpg", "jpeg", "png"])
    if img_file_buffer is not None:
        DEMO_IMAGE = img_file_buffer
    st.sidebar.markdown('---')
    # if st.sidebar.button("Use Selfie"):
    #     SELFIE_IMAGE = "./content/selfie.jpg"
    #     DEMO_IMAGE = SELFIE_IMAGE
    # st.sidebar.markdown('---')
    if st.sidebar.button("Convert to GrayScale"):
        convert_img = Image.open(DEMO_IMAGE).convert('L')
        st.image(convert_img, caption="grayScale|Just Don't Caught")
    if st.sidebar.button("Convert to RoughScale"):
        convert_img = Image.open(DEMO_IMAGE).convert('1')
        st.image(convert_img, caption="roughScale|Just Don't Caught")

    ## Leave a sample down
    st.sidebar.image(DEMO_IMAGE)
