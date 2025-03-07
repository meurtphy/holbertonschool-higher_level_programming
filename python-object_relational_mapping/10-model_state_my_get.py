#!/usr/bin/python3
"""Script that prints the State object with a given name from the database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion à MySQL en localhost:3306
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
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
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Affichage du résultat
    print(state.id if state else "Not found")

    # Fermeture de la session
    session.close()
