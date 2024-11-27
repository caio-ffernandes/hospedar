FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia a pasta Back para /app/Back dentro do contêiner
COPY ./Back /app/Back

# Copia o arquivo de dependências
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências
RUN pip install -r /app/requirements.txt

ENV PYTHONPATH=/workspace/Back


# Comando para iniciar o servidor, apontando para Back.main:app
CMD ["uvicorn", "Back.main:app", "--host", "0.0.0.0", "--port", "8080"]
