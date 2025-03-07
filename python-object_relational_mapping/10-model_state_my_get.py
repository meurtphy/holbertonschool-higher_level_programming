#!/usr/bin/python3
"""Prints the State object with the name passed as argument"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import obligatoire

if __name__ == "__main__":
    # Création de l'engine (127.0.0.1
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de l'état avec un filtre sécurisé (évite SQL Injection)
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat (format strict)
    print(state.id if state else "Not found")

    # Fermeture propre de la session
    session.close()
