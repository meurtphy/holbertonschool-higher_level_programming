#!/usr/bin/python3
"""Prints the State object with the name passed as argument"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de l'engine avec 127.0.0.1 pour éviter les erreurs de connexion
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True  # Vérifie la connexion avant exécution
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état correspondant (SQL Injection Safe)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Affichage du résultat EXACTEMENT comme demandé
    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermeture propre de la session
    session.close()
