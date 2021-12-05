# API Machine Learning

Pour utiliser l'API, il faut avoir Python 3 d'installé et utiliser les [environnements virtuels](https://docs.python.org/fr/3/library/venv.html).

```
python3 -m venv venv
# Pour Linux et macOS
source venv/bin/activate
# Pour Windows
C:\\{chemin d'accès au dossier venv}\\Scripts\\activate.bat
```

On peut ensuite installer en local les dépendances.

```
pip install --upgrade pip
pip install -r requirements.txt
```

Et il ne reste plus qu'à lancer l'API.

```
flask run
```

## Commandes Docker

Pour construire l'image Docker :

```
docker build -t api_ml_k8s .
```

Faire `docker login` pour s'authentifier à Docker Hub puis envoyer l'image dessus.

```
docker tag api_ml_k8s <DOCKER_ID>/api_ml_k8s:latest
docker push <DOCKER_ID>/api_ml_k8s:latest