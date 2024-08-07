# 💬 Chatbot - Text to Image

![Streamlit](https://img.shields.io/badge/Streamlit-0E4B8C?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FF9A00?style=for-the-badge&logo=huggingface&logoColor=white)

## Descrição

Este é um chatbot desenvolvido em Streamlit que utiliza o modelo Stable Diffusion da Hugging Face para gerar imagens a partir de prompts de texto. O aplicativo permite que os usuários insiram uma descrição de imagem e recebam uma imagem gerada pelo modelo.

## Funcionalidades

- **Chatbot Interativo:** Interface de chat para interagir com o modelo.
- **Geração de Imagens:** Gera imagens a partir de descrições de texto usando o modelo Stable Diffusion.
- **Interface Simples:** Construído com Streamlit, proporcionando uma interface amigável e fácil de usar.

## Pré-requisitos

- Python 3.7 ou superior
- Conta na Hugging Face com um token de API válido

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/jpforol/streamlit-stablediffusion
   cd streamlit-stablediffusion
   ```
2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate # No Windows, use `venv\Scripts\activate`
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Adicione seu token da Hugging Face ao arquivo `secrets.toml`:
   ```toml
   [hugging_face_token]
   api_key = "your_hugging_face_token"
   ```

## Uso

1. Execute o aplicativo Streamlit:
   ```bash
   streamlit run streamlit_app.py
   ```
2. Interaja com o chatbot, inserindo descrições de imagens e recebendo imagens geradas.
