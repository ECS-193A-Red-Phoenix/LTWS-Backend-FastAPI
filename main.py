from fastapi import FastAPI, Depends, Request
from WarningSystem import models, database, schemas
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()


models.Base.metadata.create_all(database.engine)


templates = Jinja2Templates(directory = "build")
app.mount("/static", StaticFiles(directory = "build/static"), name = "static")


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class = HTMLResponse)
async def homepage(request : Request):
    return templates.TemplateResponse("index.html", { "request" : request} )


@app.post("/input_to_db")
async def create(request: schemas.ModelInfo, db: Session = Depends(get_db)):
    print(f"Request Timestamp: {request.timestamp}")
    newly_inputted_data = models.ModelDb(timestamp = request.timestamp, map_binary = request.model_output_binaries)
    db.add(newly_inputted_data)
    db.commit()
    db.refresh(newly_inputted_data)
    return newly_inputted_data


# uvicorn main:app --reload

"""
if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)
"""
