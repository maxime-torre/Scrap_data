import requests
from bs4 import BeautifulSoup

url = "https://people.epfl.ch/emmanuel.abbe?lang=fr"

# Récupérer le contenu HTML de la page web
response = requests.get(url)
html = response.content

# Utiliser BeautifulSoup pour extraire le texte du bouton
soup = BeautifulSoup(html, 'html.parser')
button = soup.find('button', {'id': 'collapse-arrow-0'})
button_text = button.get_text(strip=True)

# Afficher le texte extrait
print(button_text)

