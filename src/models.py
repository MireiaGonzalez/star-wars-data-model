import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key = True)
    first_name = Column(String(120), nullable = False)
    last_name = Column(String(120), nullable = False)
    user_name = Column(String(120), nullable = False)
    password = Column(String(120))
    email = Column(String(120), nullable = False)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key = True)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(50))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(Integer)
    name = Column(String(120))
    image = Column(String(250))

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key = True)    
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eye_color = Column(String(20))
    birth_year = Column(String(20))
    gender = Column(String(20))
    name = Column(String(100))
    image = Column(String(250))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    planet = relationship("Planet")


class Favourite(Base):
    __tablename__ = "favourite"
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    user = relationship("User")
    character = relationship("Character")
    planet = relationship("Planet")

class Description(Base):
    __tablename__ = "description"
    id = Column(Integer, primary_key = True)
    description = Column(String(500))
    character_id = Column(Integer, ForeignKey("character.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character = relationship("Character")
    planet = relationship("Planet")


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')