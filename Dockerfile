# Usa uma imagem oficial do Python como base
FROM python:3.11-alpine

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala as dependências (se houver)
RUN pip install --no-cache-dir -r requirements.txt || true

# Comando para rodar o script principal
CMD ["python", "src/main.py"]

