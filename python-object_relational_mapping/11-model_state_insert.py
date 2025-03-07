#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to the database"""

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

    # Ajout d'un nouvel état
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'ID du nouvel état
    print(new_state.id)

    # Fermeture de la session
    session.close()
