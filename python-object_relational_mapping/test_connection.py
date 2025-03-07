#!/usr/bin/python3
import sys
from sqlalchemy import create_engine

username = "root"
password = "root"
database = "hbtn_0e_6_usa"

# Connexion via TCP avec 127.0.0.1 et port 3306
engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@127.0.0.1:3306/{database}",
    pool_pre_ping=True
)

try:
    with engine.connect() as connection:
        print("✅ Connexion réussie à MySQL !")
except Exception as e:
    print(f"❌ Erreur de connexion : {e}")
