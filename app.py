import streamlit as st
import openai
import base64
from PIL import Image
from io import BytesIO

# Setup OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

# Function to encode image to base64
def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to ask question using latest OpenAI SDK (v1+)
def ask_question_about_image(base64_image, question):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # use gpt-4 if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant. The user is asking a question about an image, but you can only answer based on the question text."},
            {"role": "user", "content": question}
        ],
        max_tokens=300,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Streamlit UI
st.title("Ask Anything About an Image 🧠")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
question = st.text_input("Ask a question about the image")

if uploaded_file and question:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    base64_image = encode_image_to_base64(image)

    if st.button("Get Answer"):
        with st.spinner("Generating answer..."):
            answer = ask_question_about_image(base64_image, question)
            st.success(answer)
