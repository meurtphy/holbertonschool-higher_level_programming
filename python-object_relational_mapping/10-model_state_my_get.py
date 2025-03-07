#!/usr/bin/python3
"""Prints the State object with the given name from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de l'engine en utilisant 127.0.0.1 pour éviter les erreurs de socket
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche stricte de l'état avec le nom passé en argument
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Vérification et affichage strictement identique à l'énoncé
    if state:
        print("{}".format(state.id))  # Affichage uniquement de l'ID
    else:
        print("Not found")

    # Fermeture propre de la session
    session.close()
