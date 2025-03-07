#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion MySQL (forcer 127.0.0.1)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Création de l'État "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'ID du nouvel État
    print(new_state.id)

    # Fermeture de la session
    session.close()
