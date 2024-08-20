import requests

class TempoAPI:
    BASE_URL = "https://www.api-couleur-tempo.fr/api/jourTempo"

    def __init__(self):
        self.headers = {
            "accept": "application/json"
        }

    def get_tempo_data(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()  # Vérifie si la requête a réussi
            data = response.json()
            code_jour = data.get('codeJour')
            couleurs = {
                0: "INDEFINI",
                1: "BLEU",
                2: "BLANC",
                3: "ROUGE"
            }
            return couleurs.get(code_jour, "INCONNU")
        except requests.exceptions.HTTPError as http_err:
            print(f"Erreur HTTP : {http_err}")
            return "INCONNU"
        except Exception as err:
            print(f"Erreur : {err}")
            return "INCONNU"

    def getTempoToday(self):
        """Retourne la couleur du jour Tempo pour aujourd'hui."""
        return self.get_tempo_data("today")

    def getTempoTomorrow(self):
        """Retourne la couleur du jour Tempo pour demain."""
        return self.get_tempo_data("tomorrow")

    def shellPlugOn(self, ip_address):
        """Allume la prise Shelly Plug S à l'adresse IP spécifiée."""
        url = f"http://{ip_address}/relay/0/on"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Vérifie si la requête a réussi
            if response.status_code == 200:
                print(f"Prise à {ip_address} allumée.")
            else:
                print(f"Impossible d'allumer la prise à {ip_address}.")
        except requests.exceptions.HTTPError as http_err:
            print(f"Erreur HTTP : {http_err}")
        except Exception as err:
            print(f"Erreur : {err}")

    def shellPlugOff(self, ip_address):
        """Éteint la prise Shelly Plug S à l'adresse IP spécifiée."""
        url = f"http://{ip_address}/relay/0/off"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Vérifie si la requête a réussi
            if response.status_code == 200:
                print(f"Prise à {ip_address} éteinte.")
            else:
                print(f"Impossible d'éteindre la prise à {ip_address}.")
        except requests.exceptions.HTTPError as http_err:
            print(f"Erreur HTTP : {http_err}")
        except Exception as err:
            print(f"Erreur : {err}")
