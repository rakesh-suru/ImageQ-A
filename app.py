import streamlit as st
import openai
import base64
from PIL import Image
from io import BytesIO

# Get API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Convert image to base64
def encode_image(image_file):
    img = Image.open(image_file)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Get caption using OpenAI Vision
def get_caption(base64_image):
    response = openai.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {"role": "user", "content": [
                {"type": "text", "text": "Describe this image in detail."},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}"}}
            ]}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content

# Streamlit UI
st.title("🧠 AI Image Describer with GPT-4")
uploaded_file = st.file_uploader("📤 Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    with st.spinner("Analyzing with GPT-4..."):
        base64_img = encode_image(uploaded_file)
        caption = get_caption(base64_img)
        st.success("Caption Generated!")
        st.markdown(f"**📝 Description:** {caption}")
