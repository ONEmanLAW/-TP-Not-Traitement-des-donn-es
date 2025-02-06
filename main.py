import requests
from bs4 import BeautifulSoup
import csv


URL = "https://www.ign.com/wikis/elden-ring/Weapons"


headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(URL, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")


    weapon_sections = soup.find_all("li", class_="wiki-list-item") 

    weapons = []


    for weapon in weapon_sections:
        name = weapon.find("a").text.strip() if weapon.find("a") else "Nom inconnu"
        link = weapon.find("a")["href"] if weapon.find("a") else "Aucun lien"
        
        weapons.append({"Nom": name, "Lien": link})

  
    with open("armes_ign.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Nom", "Lien"])
        writer.writeheader()
        writer.writerows(weapons)

    print("Scraping terminé ! Les données sont dans 'armes_ign.csv'.")

else:
    print(f"Erreur {response.status_code} lors de l'accès à la page.")
