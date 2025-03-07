#!/usr/bin/python3
"""Script that adds the State object 'Louisiana' to database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connexion avec 127.0.0.1 pour éviter les erreurs de socket
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True  # Évite les erreurs de connexion
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Créer un nouvel objet State pour Louisiana
    new_state = State(name="Louisiana")

    # Ajouter et commit
    session.add(new_state)
    session.commit()

    # Afficher l'ID du nouvel état
    print(new_state.id)

    session.close()
