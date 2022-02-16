from datetime import datetime
from pydantic import BaseModel
from fastapi import File


class ModelInfo(BaseModel):
    timestamp: str
    file: bytes
