# 🖼️🔍 Image Question Answering App

This is a simple Streamlit web app that allows you to **upload an image** and **ask questions about it**. The app will intelligently answer your queries based on the image content using **OpenAI's GPT-4 Vision** model.

## Features 🚀
- Upload any image (PNG, JPG, JPEG).
- Ask natural language questions about the image.
- Get intelligent and context-aware answers using GPT-4 Vision API.
- Minimalistic and clean Streamlit interface.

## Tech Stack 🛠️
- **Streamlit** — For the frontend web interface.
- **OpenAI GPT-4 Vision** — For understanding and reasoning over images.
- **Python (Pillow)** — For image processing and encoding.

## Installation & Running Locally 🖥️
1. Clone/Download the repository and navigate to the project folder.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Replace `YOUR_OPENAI_API_KEY` in `app.py` with your actual OpenAI API Key.
4. Run the app:
    ```bash
    streamlit run app.py
    ```
5. The app will open in your browser at `http://localhost:8501/`.

## Notes ⚡
- Ensure you have GPT-4 Vision API access.
- You can extend this app to add voice inputs, multi-turn conversations, or deploy it on Streamlit Cloud.

---

Made with ❤️ using GPT-4 Vision and Streamlit.