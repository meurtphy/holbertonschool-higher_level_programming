#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion MySQL avec pool_pre_ping
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Création session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Ajout de "Louisiana"
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Affichage de l'id du nouvel élément
    print(f"{new_state.id}")

    session.close()
