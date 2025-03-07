#!/usr/bin/python3
"""Prints the State object with the given name from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de l'engine en forçant l'IP 127.0.0.1 pour éviter les erreurs
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche du premier état correspondant EXACTEMENT au nom donné
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Affichage strictement identique à l'exemple attendu
    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermeture propre de la session
    session.close()
