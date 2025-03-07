#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connexion à MySQL en localhost:3306
    engine = create_engine(
        "mysql+mysqldb://{}:{}@127.0.0.1:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération de l'état avec le nom spécifié (évite SQL Injection)
    state_name = sys.argv[4]
    state = session.query(State).filter(State.name == state_name).first()

    # Affichage du résultat
    if state:
        print(state.id)
    else:
        print("Not found")

    # Fermeture de la session
    session.close()
