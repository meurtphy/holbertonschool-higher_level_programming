#!/usr/bin/python3
"""Script that lists all State objects containing 'a' from database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Création de l'engine avec pool_pre_ping activé
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération des États contenant 'a'
    states = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .order_by(State.id)
        .all()
    )

    # Affichage des résultats
    for state in states:
        print(f"{state.id}: {state.name}")

    # Fermeture de la session
    session.close()
