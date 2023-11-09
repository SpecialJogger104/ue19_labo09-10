import requests

# URL de l'API OpenSky Network pour récupérer les vols au-dessus de la Belgique
api_url = "https://opensky-network.org/api/states/all?lamin=49.4966&lomin=2.5464&lamax=51.5051&lomax=6.4073"

# Envoie de la requête GET à l'API
response = requests.get(api_url)

# Vérification de la réussite de la requête
if response.status_code == 200:

    data = response.json()

    # Récupération du nombre de vols au-dessus de la Belgique
    num_flights = len(data["states"])

    print(f"Nombre de vols au-dessus de la Belgique : {num_flights}")
else:
    print(f"Échec de la requête. Code de statut : {response.status_code}")
print('') 
