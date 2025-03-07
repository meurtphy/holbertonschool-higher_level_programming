#!/usr/bin/python3
"""Script that deletes all State objects with 'a' in name from database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion à la base de données
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Sélection des états contenant la lettre "a"
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Suppression des états sélectionnés
    for state in states_to_delete:
        session.delete(state)

    # Validation des modifications
    session.commit()

    # Fermeture de la session
    session.close()
