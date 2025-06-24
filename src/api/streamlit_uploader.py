import streamlit as st
import tempfile
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.ocr.ocr_processor import run_ocr_on_image



# from utils.logger import get_logger
# from s3.s3_uploader import upload_file_to_s3
# from .env import S_BucketName, S_Region

# logger = get_logger("Running Streamlit")

# BUCKET_NAME = S_BucketName
# REGION_NAME = S_Region 

LOCAL_SAVE_DIR = "data/raw"
os.makedirs(LOCAL_SAVE_DIR, exist_ok=True)

st.set_page_config(page_title="Streamlit Uploader", layout="centered")
st.title("📄DocuMind-AI - Upload a Document")

uploaded_file = st.file_uploader(
    "Upload your file...", 
    type=["pdf", "jpg", "jpeg", "png", "tiff", "bmp", "gif", "webp", "txt", "docx", "csv"]
    )

if uploaded_file is not None:
    # st.success(f"✅ File selected: {uploaded_file.name}")

    if st.button("Save & Extract"):
        save_path = os.path.join(LOCAL_SAVE_DIR, uploaded_file.name)

        with open(save_path, 'wb') as f:
            f.write(uploaded_file.getvalue())
        
        st.success(f"🎉 File saved to local folder: `{save_path}`")
        print(f"\n\n{run_ocr_on_image(save_path)}\n\n")
        st.write(run_ocr_on_image(save_path))

    # if st.button("Upload to S3"):

    #     with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
    #         tmp_file.write(uploaded_file.getvalue())
    #         tmp_file_path = tmp_file.name

        # with open(tmp_file_path, 'rb') as f:
        #     result = upload_file_to_s3(f, BUCKET_NAME, f"uploads/{uploaded_file.name}")



    