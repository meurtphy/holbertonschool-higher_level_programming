#!/usr/bin/python3
"""Script that prints all City objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    # Connexion à la base de données MySQL
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ), pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération des villes avec leur état correspondant
    cities = (
        session.query(City, State)
        .join(State, City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Affichage des résultats
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session
    session.close()
