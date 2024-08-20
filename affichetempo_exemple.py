from tempo_lib import TempoAPI

def main():
    tempo_api = TempoAPI()
    
    couleur_today = tempo_api.getTempoToday()
    couleur_tomorrow = tempo_api.getTempoTomorrow()
    
    print(f"Couleur d'aujourd'hui : {couleur_today}")
    print(f"Couleur de demain : {couleur_tomorrow}")

if __name__ == "__main__":
    main()