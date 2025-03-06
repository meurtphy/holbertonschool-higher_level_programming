#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connexion à la base de données avec MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Création de la session SQLAlchemy
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération du premier état (sans récupérer toute la table)
    first_state = session.query(State).order_by(State.id).first()

    # Affichage du résultat
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Fermeture de la session
    session.close()
