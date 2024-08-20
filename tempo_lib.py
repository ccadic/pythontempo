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
