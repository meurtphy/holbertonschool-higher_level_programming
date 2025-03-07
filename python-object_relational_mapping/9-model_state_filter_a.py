#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de l'engine avec 127.0.0.1 pour éviter les erreurs MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True  # Evite les problèmes de connexion
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête pour filtrer les États contenant la lettre 'a'
    states = session.query(State).filter(
        State.name.like("%a%")
    ).order_by(State.id).all()

    # Affichage EXACTEMENT comme demandé
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture propre de la session
    session.close()
