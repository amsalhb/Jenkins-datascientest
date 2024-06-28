from typing import Union
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Bonjour": "We Love Datascientest, We build a CI/CD Pipeline !!"}
