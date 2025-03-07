#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion à MySQL avec 127.0.0.1 pour éviter les erreurs de socket
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête : récupérer les États contenant 'a', triés par ID croissant
    states = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .order_by(State.id)
        .all()
    )

    # Affichage strictement identique à l'exemple
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Fermeture propre de la session
    session.close()
