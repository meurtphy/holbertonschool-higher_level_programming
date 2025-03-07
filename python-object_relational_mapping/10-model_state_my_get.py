#!/usr/bin/python3
"""Script that prints the State object with given name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion avec 127.0.0.1 pour éviter les erreurs de socket
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche de l'état par nom
    state_name = sys.argv[4].strip()
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
