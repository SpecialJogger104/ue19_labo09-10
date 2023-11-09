# Utilisez une image Python officielle en tant qu'image de base
FROM python:3.8-slim

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le script Python et le fichier requirements.txt dans le conteneur
COPY app.py .
COPY requirements.txt .

# Installez les dépendances définies dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter le script Python quand le conteneur démarre
CMD ["python", "app.py"]
