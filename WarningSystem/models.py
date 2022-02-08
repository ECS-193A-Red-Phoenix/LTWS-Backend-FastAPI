from .database import Base
from sqlalchemy import Column, DateTime, BLOB, TEXT


class ModelDb(Base):
    __tablename__ = "Hydrodynamic Model Output Binaries"
    timestamp = Column(DateTime, primary_key = True, index = True)  # datetime.now(timezone.utc)
    map_binary = Column(BLOB)  # holds binaries for map creation

