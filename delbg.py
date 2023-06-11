import streamlit as st
import time
import warnings
import torch        # Don't ask
import onnxruntime  # Won't tell (joking; fixes troubles with gpu access in some instances)
from rembg import remove
from PIL import Image


warnings.filterwarnings("ignore")
st.title("Remove Background")
st.divider()
uploaded_file = st.file_uploader("Upload a png file to remove background", type="png")

if uploaded_file:
    st.image(uploaded_file, caption='Original')
    if st.button("Remove"):
        with st.spinner("Removing..."):
            input = Image.open(uploaded_file)
            output = remove(input)
            now = str(time.strftime("%Y%m%d-%H%M%S"))
            filename = now + ".png"
            output.save(filename)
            st.image(output, caption='Result')

