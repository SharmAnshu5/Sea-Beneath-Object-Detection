# frontend/app.py
import streamlit as st

st.set_page_config("SeaBeneath Live", layout="centered")
st.title("🌊 SeaBeneath – Live Underwater Detection")

tab1, tab2 = st.tabs(["📸 Live Camera", "📁 Upload Image"])
with tab1:
    st.markdown("Live feed with YOLOv8 detection.")
    st.image("http://localhost:8000/live", use_container_width=True)

with tab2:
    upload = st.file_uploader("Upload underwater image", type=["png", "jpg", "jpeg"])
    conf = st.slider("Confidence threshold", 0.1, 1.0, 0.4)
    if upload:
        with st.spinner("Detecting objects..."):
            response = requests.post(
                "http://localhost:8000/detect/upload",
                files={"file": upload},
                data={"conf": conf}
            )
        if response.status_code == 200:
            st.image(response.content, caption="🧠 Detected Output", use_container_width=True)
        else:
            st.error("❌ Detection failed.")
