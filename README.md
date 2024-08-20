# pythontempo
Librairie python pour permettre de récupérer la couleur du tarif tempo, basée sur un travail de https://www.api-couleur-tempo.fr/api

Fonctionne avec python 3.1x

Pensez à installer: pip install requests

<img src="https://github.com/ccadic/pythontempo/blob/main/tempolib.jpg">


**Explication du code**
Importation de la librairie tempo_lib : Le script commence par importer la classe TempoAPI depuis votre librairie tempo_lib.py.

Vérification des heures creuses : La fonction is_in_heures_creuses vérifie si l'heure actuelle se situe entre 22h et 6h.

**Contrôle des prises Shelly :**

Couleur Tempo : Le script appelle getTempoToday() pour obtenir la couleur Tempo du jour.

Heures creuses : Le script vérifie si l'heure actuelle se situe dans la plage des heures creuses.

Allumage ou extinction des prises : Si la période est BLEU et que l'heure est dans les heures creuses, les prises sont allumées. Sinon, elles sont éteintes. Le script affiche un message pour chaque action effectuée.

Exécution du script : Lorsque le script est exécuté, il utilise la classe TempoAPI de votre librairie pour effectuer les actions nécessaires en fonction de la couleur Tempo et de l'heure actuelle.

**Exemple de sortie possible**
En fonction de la période et de l'heure, voici ce que vous pourriez voir lorsque vous exécutez le script :

**Heure actuelle : 23:15:30**
Couleur Tempo aujourd'hui : BLEU
Période BLEU et heures creuses. Allumage des prises.
Prise à 192.168.1.100 allumée.
Prise à 192.168.1.101 allumée.
Ou si on est hors des heures creuses ou si la période n'est pas BLEU :

**Heure actuelle : 08:30:00**
Couleur Tempo aujourd'hui : BLEU
Sortie des heures creuses.
Prise à 192.168.1.100 éteinte.
Prise à 192.168.1.101 éteinte.
Ce script utilise maintenant correctement la librairie tempo_lib.py pour gérer les prises Shelly en fonction des périodes tarifaires et des heures creuses.
