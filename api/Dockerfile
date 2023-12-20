# Utiliza una imagen base oficial de Python
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Actualiza pip
RUN pip install --upgrade pip

# Copia el archivo de requisitos y lo instala
COPY ./app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de tu código de aplicación al directorio de trabajo
COPY ./app/ .
