from fastapi import FastAPI, File
from WarningSystem import models, database
# from sqlalchemy.orm import Session

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
def create(file: bytes = File(default=None)):
    f = open("plane_2", "wb")
    f.write(file)
    f.close()

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
"""
