#FastAPI application setup & routes

from fastapi import FastAPI
app = FastAPI()


@app.get("/Tickets")
def read_root():
  return {"Hello": "World"}
