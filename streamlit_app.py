import streamlit as st
import requests
import io
from PIL import Image


def query_stabilitydiff(payload, headers):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


st.title("💬 Chatbot - Texto para Imagem")
st.caption("🚀 Uma aplicação de Chatbot com Streamlit com tecnologia Stable Diffusion")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {
            "role": "assistant",
            "content": "Que tipo de imagem você precisa?",
        }
    ]

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])
    if "image" in message:
        st.chat_message("assistant").image(
            message["image"], caption=message["prompt"], use_column_width=True
        )

if prompt := st.chat_input():

    if "api_key" not in st.secrets["hugging_face_token"]:
        st.info("Please add your Hugging Face Token to continue.")
        st.stop()

    # Prompt de Entrada
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # COnsulta para Stable Diffusion
    headers = {"Authorization": f"Bearer {st.secrets.hugging_face_token.api_key}"}
    image_bytes = query_stabilitydiff(
        {
            "inputs": prompt,
        },
        headers,
    )

    # Imagem de Retorno
    image = Image.open(io.BytesIO(image_bytes))
    msg = f'Aqui está sua imagem relacionada a "{prompt}"'

    # Apresentar Resultado
    st.session_state.messages.append(
        {"role": "assistant", "content": msg, "prompt": prompt, "image": image}
    )
    st.chat_message("assistant").write(msg)
    st.chat_message("assistant").image(image, caption=prompt, use_column_width=True)
