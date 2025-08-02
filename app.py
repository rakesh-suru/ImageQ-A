import streamlit as st
import openai
from PIL import Image
import base64
from io import BytesIO

# ==== CONFIG ====
openai.api_key = 'YOUR_OPENAI_API_KEY'  # <-- Replace with your API Key

# ==== FUNCTIONS ====
def encode_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return img_str

def ask_question_about_image(base64_image, user_question):
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_question},
                    {"type": "image_url", "image_url": f"data:image/png;base64,{base64_image}"}
                ]
            }
        ],
        max_tokens=500
    )
    return response.choices[0].message.content

# ==== STREAMLIT UI ====
st.set_page_config(page_title="Ask Anything About Image", layout="centered")
st.title("🖼️🔍 Ask Anything About an Image")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    question = st.text_input("Type your question about this image:")

    if st.button("Get Answer") and question:
        with st.spinner("Thinking..."):
            base64_image = encode_image_to_base64(image)
            answer = ask_question_about_image(base64_image, question)
        st.success("Answer:")
        st.write(answer)