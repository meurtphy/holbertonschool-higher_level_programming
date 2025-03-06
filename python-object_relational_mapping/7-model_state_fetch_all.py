#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Création du moteur SQLAlchemy (connexion à MySQL)
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération et affichage des États triés par id
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")

    # Fermeture de la session
    session.close()
