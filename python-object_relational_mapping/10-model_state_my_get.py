#!/usr/bin/python3
"""Prints the State object with the name passed as argument"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion MySQL avec 127.0.0.1 pour éviter l'erreur de socket
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de l'État correspondant au nom donné en argument (SQL injection free)
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermeture de la session
    session.close()
