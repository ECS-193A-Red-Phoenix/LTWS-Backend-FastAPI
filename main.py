from fastapi import FastAPI, Depends, Request, UploadFile, File
from WarningSystem import models, database, schemas
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from os import path, listdir
from collections import deque
from typing import Deque, List
from datetime import datetime

from utility import utilities


DISK_ENTRIES : Deque[str] = deque()  # Deque[File Names in Disk]


app = FastAPI()


models.Base.metadata.create_all(database.engine)


templates = Jinja2Templates(directory = "build")
app.mount("/build", StaticFiles(directory = "build/static"), name = "static")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class = HTMLResponse)
async def homepage(request : Request):
    return templates.TemplateResponse("index.html", { "request" : request} )


"""
@app.post("/input_to_db")
async def create(request: schemas.ModelInfo, db: Session = Depends(get_db)):
    print(f"Request Timestamp: {request.timestamp}")
    newly_inputted_data = models.ModelDb(timestamp = request.timestamp, map_binary = request.model_output_binaries)
    db.add(newly_inputted_data)
    db.commit()
    db.refresh(newly_inputted_data)
    return newly_inputted_data
"""

# Receives a file and saves it to disk
@app.post("/input_to_disk", tags  = ["files"])
async def create(uploaded_file: UploadFile = File(...)):
    if len(DISK_ENTRIES) == 200:  # 2 week worth of visualizations should be stored on the disk
        # disk is full 
        file_to_remove_from_disk = DISK_ENTRIES.popleft()
        err : int = utility.remove_file_from_disk(file_to_remove_from_disk)
        if err != 1:
            print(f"File: {file_to_remove_from_disk} does not exist")
    
    print("executed till here")
    DISK_ENTRIES.append(uploaded_file.filename)

    file_location_in_disk = f"./disk_file_storage/{uploaded_file.filename}"

    # Copy file contents to new file with same name on disk
    file_contents = uploaded_file.file.read()
    local_file = open(file_location_in_disk, "wb+")
    local_file.write(file_contents)
    local_file.close()

    print(f"LENGTH OF QUEUE: {len(DISK_ENTRIES)}")

    return {
        "filename" : uploaded_file.filename
    }


# Retrieve all visualizations from certain date onwards
@app.get("/retrieve_visualizations/{date}")
async def querying_from_disk(date: datetime):
    


    # query both temperature and flow subdirectories
    pass


@app.get("/clear_disk")
def clear_disk() -> None:
    disk_location : str = "./disk_file_storage/" 
    files_in_disk : List[str] = listdir(disk_location)
    print("ITERATING THROUGH FILES IN DISK:")
    print("================================")
    for file_name in files_in_disk:
        print(file_name.split(" "))
        err = utilities.remove_file_from_disk(file_name = file_name)
        if err != 1:
            print("error occured")

    

# uvicorn main:app --reload

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="localhost", port=8000, reload=True)
"""
