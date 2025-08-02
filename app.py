import streamlit as st
import openai
import base64
from PIL import Image
import io
import os

# Set API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to convert image to base64
def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.read()).decode('utf-8')

# Ask question about image using GPT-4 with Vision
def ask_question_about_image(base64_image, user_question):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="Image Q&A with GPT-4 Vision", layout="centered")
st.title("🖼️ Ask Anything About Your Image")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
question = st.text_input("What do you want to know about this image?")

if uploaded_file and question:
    with st.spinner("Analyzing image..."):
        try:
            base64_image = encode_image(uploaded_file)
            answer = ask_question_about_image(base64_image, question)
            st.success("Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"Error: {e}")
