#!/usr/bin/python3
"""
python file that contains the class defination of a
State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class"""

    __tablename__ = 'states'
    id = Column(Integr, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
