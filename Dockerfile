# Usa imagem leve do Python
FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Instala dependências do sistema que o pip pode precisar
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos da aplicação para o container
COPY . /app

# Instala as dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para iniciar a aplicação Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
