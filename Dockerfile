# Image de base
FROM ubuntu:latest

# Installation de Python 3 and pip3
RUN apt update
RUN apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt update && \
    apt install python3.8 python3-pip -y


# Mise à jour de pip3
RUN pip3 install --upgrade pip

RUN mkdir /app
WORKDIR /app
# Copie des fichiers
COPY requirements.txt /app
COPY app.py /app
COPY artifacts/ /app/artifacts/
COPY src/ /app/src/
RUN pip3 install --no-cache-dir -r requirements.txt

# On ouvre et expose le port 80
EXPOSE 80

# Lancement de l'API
CMD ["gunicorn", "app:app", "run", "-b", "0.0.0.0:80", "-w", "4"]