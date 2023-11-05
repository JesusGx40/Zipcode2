# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios para tu aplicación (asegúrate de incluir tu requirements.txt)
COPY . /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requeriments.txt

# Expone el puerto en el que se ejecuta tu aplicación
EXPOSE 8000

# Comando para ejecutar tu aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]