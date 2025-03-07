#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Script that prints the State object with given name"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine with pool_pre_ping=True to avoid connection issues
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query state by name (ensure no trailing spaces)
        state = session.query(State).filter(
            State.name == sys.argv[4].strip()
        ).first()

        # Print state ID if found, otherwise print "Not found"
        print(state.id if state else "Not found")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close session
        session.close()
