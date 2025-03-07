#!/usr/bin/python3
"""Script that prints the State object with given name"""

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

    # Recherche stricte du nom
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Affichage propre
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
