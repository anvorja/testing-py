# Utiliza la imagen oficial de Python como base
FROM python:3.8

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY operaciones.py tests.py requirements.txt /app/

# Instala las dependencias
RUN pip install -r requirements.txt

# Ejecuta las pruebas cuando se inicia el contenedor
CMD ["python", "tests.py"]
