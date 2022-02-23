from fastapi import FastAPI, Depends, File, Response, UploadFile
from WarningSystem import models, database
from sqlalchemy.orm import Session
import datetime
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware


#  for frontend endpoint testing
from pathlib import Path
base_url = f"{Path.cwd()}/communication_scripts/binaries/"
test_images = [f"{base_url}/p2.png", f"{base_url}/picture1.png"]


app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["GET"],
    allow_headers = [
        "Content-Type",
        "application/json"
    ]
)

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def homepage():
    print("IN HOMEPAGE!")
    return {
        "data" : "WELCOME TO THE LTWS HOMEPAGE"
    }


@app.post("/input_to_db", tags  = ["files"])
async def create(file : bytes = File(default = None), db: Session = Depends(get_db)):
    # f = open("plane_2", "wb+")
    # f.write(file)
    # f.close()
    time = datetime.datetime.now(datetime.timezone.utc)   
    newly_inputted_data = models.Visualizations(timestamp = time, map_binary = file)
    db.add(newly_inputted_data)
    db.commit()
    db.refresh(newly_inputted_data)
    return {
        "filename" : "LOOKS GOOD"
    }


@app.get("/frontend_get_image_test/{id}")
async def frontend_get_image_test(id : int = 0): # request, db : Session  = Depends(get_db)):
    return FileResponse(
        test_images[id]
    )




async def database_clear() -> int:
    # after post we will need to create a db clear functionality
    # -> sliding window technique to deleting data
    pass



# uvicorn main:app --reload

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
"""
