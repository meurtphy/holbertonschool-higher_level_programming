#!/usr/bin/python3
"""Script that prints the State object with given name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion MySQL avec 127.0.0.1
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche SQLAlchemy avec un filtre insensible à la casse
    state = session.query(State).filter_by(name=sys.argv[4]).first()

    # Affichage
    print(state.id if state else "Not found")

    session.close()
