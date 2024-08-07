import streamlit as st
import requests
import io
from PIL import Image
from deep_translator import GoogleTranslator


def query_stabilitydiff(model, payload, headers):
    API_URL = "https://api-inference.huggingface.co/models/" + model
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


# Instancia do Tradutor
tradutor = GoogleTranslator(source="pt", target="en")


st.title("💬 Chatbot - Texto para Imagem")
st.caption(
    "🚀 Uma aplicação de Chatbot com Streamlit com tecnologia de Geração de Imagens a partir de modelos de IA"
)
st.session_state.option_model = st.selectbox(
    "Selecione o modelo:",
    (
        "stabilityai/stable-diffusion-xl-base-1.0",
        "alvdansen/littletinies",
        "alvdansen/phantasma-anime",
        "alvdansen/frosting_lane_redux",
    ),
)

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
    print(tradutor.translate(prompt))
    st.session_state.messages.append(
        {"role": "user", "content": tradutor.translate(prompt)}
    )
    st.chat_message("user").write(prompt)

    with st.spinner("Carregando sua Imagem..."):

        # Consulta para Stable Diffusion
        headers = {"Authorization": f"Bearer {st.secrets.hugging_face_token.api_key}"}
        image_bytes = query_stabilitydiff(
            st.session_state.option_model,
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

        # Botão de Download
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.download_button(
            label="Download Imagem",
            data=byte_im,
            file_name=f"image.png",
            mime="image/png",
        )
