import streamlit as st
from PIL import Image
import base64
import openai
import io

# Set up OpenAI API Key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

def ask_question_about_image(base64_image, question):
    response = openai.ChatCompletion.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        },
                    },
                ],
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message["content"]

st.title("🖼️ Ask a Question About an Image")
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    question = st.text_input("Enter your question about the image:")
    if st.button("Get Answer") and question:
        with st.spinner("Getting answer from GPT..."):
            base64_image = image_to_base64(image)
            answer = ask_question_about_image(base64_image, question)
            st.success(answer)
