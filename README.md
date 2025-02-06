# Guide d'utilisation du projet de Scraping de Notes de Jeux

Ce projet a pour but de récupérer des informations sur des jeux vidéo à partir d'une API, l'API IGDB et puis d'aller chercher les notes de ces jeux sur le site IGN en scapant. Voici comment procéder pour l'utiliser.

## Étapes à suivre

### 1. **Lancer le script Python (main.py)**

Le script `main.py` est utilisé pour récupérer des informations de base sur 20 jeux vidéo depuis l'API **IGDB**. Ces informations incluent des données telles que le nom du jeu, sa date de sortie, son résumé, ses genres, et ses plateformes. Il est important de commencer par exécuter ce script, car il génère un fichier CSV avec toutes les informations dont nous avons besoin pour récupérer les notes des jeux.

#### Comment l'utiliser :
1. Ouvre un terminal dans le dossier du projet.
```bash
   pip install requests python-dotenv
````
2. Exécute la commande suivante pour lancer le script Python et récupérer les informations des jeux :

   ```bash
   python main.py

3. Install.

  ```bash
  npm install axios cheerio csv-parser
  ````
&&

  ```bash
  node scraper.js
  ````

Si jamais le test.js et uniquement un test pour voir si c'était fonctionnel.

4. Fichier CSV des jeux récupérés
Le fichier games.csv contient les informations de base sur les jeux, récupérées depuis l'API IGDB.
Le fichier game_ratings_with_notes.csv contient les notes des jeux récupérées depuis IGN

5. Explication des fichiers CSV
Le fichier games.csv contient les colonnes suivantes :

Nom 
Résumé
Date de sortie
Genres 
Plateformes 
Le fichier game_ratings_with_notes.csv contient deux colonnes principales :

Nom :
Note : La note des utilisateurs récupérée sur IGN.

6. Points importants à noter
Séquence d'exécution : Il est important de suivre l'ordre des étapes. Il faut d'abord exécuter main.py pour récupérer les informations des jeux, puis seulement exécuter scraper.js pour obtenir les notes des jeux.
Structure des fichiers : Les fichiers CSV générés sont automatiquement sauvegardés dans le répertoire où s'exécutes les scripts.
Dépendances nécessaires : Le script scraper.js utilise des dépendances externes telles que axios, cheerio et csv-parser. Assure-vous d'avoir installé ces dépendances avant d'exécuter le script.


