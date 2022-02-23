from time import time
from .database import Base
from sqlalchemy import Column, DateTime, BLOB, FLOAT


class Visualizations(Base):
    __tablename__ = "Hydrodynamic Model Output Binaries"
    timestamp = Column(DateTime, primary_key = True, index = True)  # datetime.now(timezone.utc)
    map_binary = Column(BLOB)  # holds binaries for map creation


class NearShoreData(Base):
    __tablename__ = "Near Shore Station Data"
    timestamp = Column(DateTime, primary_key = True, index = True)  # datetime.now(timezone.utc)
    water_temperature = Column(FLOAT)
    wave_height = Column(FLOAT)


class NasaBuoy(Base):
    __tablename__ =  "Nasa Buoy Data"
    timestamp = Column(DateTime, primary_key = True, index = True)  # datetime.now(timezone.utc)
    water_temperature = Column(FLOAT)
    wind_speed = Column(FLOAT)
    wind_direction = Column(FLOAT)
