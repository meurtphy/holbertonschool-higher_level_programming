#!/usr/bin/python3
import sys
from sqlalchemy import create_engine

# Configuration de connexion
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Test de connexion
try:
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@127.0.0.1:3307/{database}",
        pool_pre_ping=True
    )
    connection = engine.connect()
    print("Connexion réussie à MySQL!")
    connection.close()
except Exception as e:
    print(f"Erreur de connexion: {e}")
