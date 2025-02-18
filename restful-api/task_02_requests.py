import requests
import csv

def fetch_and_print_posts():
    """Récupère et affiche les titres des posts depuis JSONPlaceholder."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    # Affiche le code de statut
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # Convertit la réponse en JSON
        # Affiche les titres des posts
        for post in posts:
            print(post['title'])
    else:
        print("Échec de la requête")


def fetch_and_save_posts():
    """Récupère les posts et les sauvegarde dans un fichier CSV."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()

        # Prépare les données sous forme de liste de dictionnaires
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Écrit les données dans un fichier CSV
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()  # Écrit l'en-tête (colonnes)
            writer.writerows(data)  # Écrit les lignes (chaque post)

        print("Les posts ont été sauvegardés dans posts.csv.")
    else:
        print("Échec de la requête")


# Test des fonctions (comme montré dans main_02_requests.py)
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
