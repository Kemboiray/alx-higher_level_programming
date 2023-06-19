#!/usr/bin/python3
"""Defines a class ``State`` that inherits from ``Base`` """

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Class to which the sql table ``states`` is mapped """

    __tablename__ = 'states'
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
