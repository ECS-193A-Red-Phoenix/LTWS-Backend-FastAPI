from datetime import datetime
from pydantic import BaseModel
from fastapi import File, UploadFile


class ModelInfo(BaseModel):  # ignore this for now
    timestamp : datetime =  None
    file_binaries : UploadFile = None


class NearShoreData(BaseModel):
    timestamp : datetime =  None
    water_temperature : float = 0.0
    wave_height : float = 0.0


class NasaBuoy(BaseModel):
    timestamp: datetime =  None
    water_temperature : float = 0.0
    wind_speed : float = 0.0
    wind_direction : float = 0.0
