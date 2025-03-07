#!/usr/bin/python3
"""
Contains the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Création d'une instance de Base
Base = declarative_base()


class State(Base):
    """Représente la table `states` en SQLAlchemy"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
