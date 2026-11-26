import streamlit as st

st.set_page_config(
    page_title="TRI_NOVA_KRISHIAI",
    page_icon="🌱",
    layout="wide"
)

st.title("🌱 TRI_NOVA_KRISHIAI")

st.subheader("AI Powered Smart Agriculture System")

st.write(
    "Welcome to our AI-based Plant Disease Detection System."
)

st.info("Our 15-class AI model is under development.")

uploaded_file = st.file_uploader(
    "Upload a plant leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Plant Image")
    st.success("Image uploaded successfully!")