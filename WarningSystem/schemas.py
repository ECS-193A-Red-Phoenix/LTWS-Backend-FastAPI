from datetime import datetime
from pydantic import BaseModel
from fastapi import File


class ModelInfo(BaseModel):
    timestamp: datetime =  None
    binaries_file: bytes = File(...)
    