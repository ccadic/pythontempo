from tempo_lib import TempoAPI
from datetime import datetime, time

def is_in_heures_creuses(current_time):
    """Vérifie si l'heure actuelle est dans la période des heures creuses (22h-6h)."""
    return time(22, 0) <= current_time or current_time < time(6, 0)

def control_shelly_plugs(tempo_api, ip_addresses):
    couleur_today = tempo_api.getTempoToday()
    current_time = datetime.now().time()

    print(f"Heure actuelle : {current_time}")
    print(f"Couleur Tempo aujourd'hui : {couleur_today}")

    in_heures_creuses = is_in_heures_creuses(current_time)
    if couleur_today == "BLEU" and in_heures_creuses:
        print("Période BLEUE et heures creuses. Allumage des prises.")
        for ip in ip_addresses:
            tempo_api.shellPlugOn(ip)
    else:
        if couleur_today != "BLEU":
            print("Sortie de période BLEUE.")
        if not in_heures_creuses:
            print("Sortie des heures creuses.")
        for ip in ip_addresses:
            tempo_api.shellPlugOff(ip)

if __name__ == "__main__":
    # Liste des adresses IP des prises Shelly Plug S
    ip_addresses = ["192.168.1.100", "192.168.1.101"]

    tempo_api = TempoAPI()
    control_shelly_plugs(tempo_api, ip_addresses)
