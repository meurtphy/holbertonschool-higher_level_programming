#!/usr/bin/python3
"""Script that prints the State object with given name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion à MySQL (127.0.0.1 pour éviter les erreurs)
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Recherche SQLAlchemy (exact match, sensible à la casse)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Affichage du résultat
    print(state.id if state else "Not found")

    session.close()
