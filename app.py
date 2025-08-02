import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Load model and processor once
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# App title and instructions
st.title("🧠 Free Image Caption Generator (BLIP)")
st.markdown("Upload an image, and the BLIP model will describe it for you!")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Caption generation
    with st.spinner("Generating caption..."):
        inputs = processor(images=image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)

    st.success("✅ Caption Generated!")
    st.markdown(f"**📝 Description:** {caption}")
