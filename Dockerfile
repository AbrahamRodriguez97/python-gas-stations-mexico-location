# 1. Usar una imagen base de Python ligera
FROM python:3.11-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar los archivos necesarios al contenedor
COPY requirements.txt .
COPY data/ ./data/
COPY src/ ./src/

# 4. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Exponer el puerto que usa Streamlit (8501 por defecto)
EXPOSE 8501

# 6. Comando para ejecutar la app al iniciar el contenedor
CMD ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]