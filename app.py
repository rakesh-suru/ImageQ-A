import streamlit as st
import openai
import base64
from PIL import Image
from io import BytesIO

# Load OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_api_key"]

# Function to encode image to base64
def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Function to ask a question using GPT-3.5 (no image input)
def ask_question_about_image(base64_image, question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. The user will ask a question related to an image, but since you cannot see images, give a general, helpful answer based only on the question."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

# ==== Streamlit UI ====
st.title("Ask Anything About an Image 🖼️")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
question = st.text_input("Enter your question about the image")

if uploaded_file and question:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    base64_image = encode_image_to_base64(image)

    if st.button("Get Answer"):
        with st.spinner("Thinking..."):
            answer = ask_question_about_image(base64_image, question)
            st.success(answer)
