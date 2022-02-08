from fastapi import FastAPI, Depends, File, UploadFile
from WarningSystem import models, database
from sqlalchemy.orm import Session
import datetime


app = FastAPI()


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
async def create(map_binary: UploadFile = File(...), db: Session = Depends(get_db)):
    time = datetime.datetime.now(datetime.timezone.utc)
    file2store = await map_binary.read()
    newly_inputted_data = models.ModelDb(timestamp = time, map_binary = file2store)
    db.add(newly_inputted_data)
    db.commit()
    db.refresh(newly_inputted_data)
    return {
        "filename" : map_binary.filename,
    }


# uvicorn main:app --reload

# after post we will need to create a db clear functionality
# -> sliding window technique to deleting data

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
"""
