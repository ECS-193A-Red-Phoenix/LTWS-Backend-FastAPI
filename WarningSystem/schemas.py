from datetime import datetime
from pydantic import BaseModel
from fastapi import File, UploadFile


class ModelInfo(BaseModel):
    timestamp: datetime =  None
    file_binaries: UploadFile = None


# ignore this for now