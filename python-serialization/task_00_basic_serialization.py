#!/usr/bin/env python3
"""Module pour sérialiser un dictionnaire Python en JSON et le sauvegarder dans un fichier."""

import json  # Import du module json

def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python en JSON et l'enregistre dans un fichier.

    :param data: Dictionnaire à sérialiser.
    :param filename: Nom du fichier dans lequel enregistrer les données.
    """
    try:
        # Ouvrir le fichier en mode écriture ('w') et sérialiser les données
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Données sauvegardées dans {filename}")

    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")