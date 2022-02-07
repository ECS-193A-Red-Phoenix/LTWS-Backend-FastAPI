from fastapi import FastAPI, Depends
from WarningSystem import models, database, schemas
from sqlalchemy.orm import Session


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


@app.post("/input_to_db")
def create(request: schemas.ModelInfo, db: Session = Depends(get_db)):
    print(f"Request Timestamp: {request.timestamp}")
    newly_inputted_data = models.ModelDb(timestamp = request.timestamp, map_binary = request.model_output_binaries)
    print("422 is thrown before this line 1")
    db.add(newly_inputted_data)
    print("422 is thrown before this line 2")
    db.commit()
    print("422 is thrown before this line 3")
    db.refresh(newly_inputted_data)
    print("422 is thrown before this line 4")
    return newly_inputted_data


# uvicorn main:app --reload

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
"""
