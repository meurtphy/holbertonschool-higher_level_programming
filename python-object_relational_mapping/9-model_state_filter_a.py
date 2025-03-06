#!/usr/bin/python3
"""
Lists all State objects with 'a' in their name from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création d'une session SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête : Sélectionner les États contenant la lettre "a"
    states_with_a = (
        session.query(State)
        .filter(State.name.ilike('%a%'))
        .order_by(State.id)
        .all()
    )

    # Affichage des résultats
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Fermeture de la session
    session.close()
