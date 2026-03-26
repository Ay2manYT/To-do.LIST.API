from pydantic import BaseModel

from fastapi import FastAPI
import json, os

app = FastAPI()
FILE = "data.json"

def read():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def write(data):
    json.dump(data, open(FILE, "w"), indent=2)

class Notat(BaseModel): 
    title:str
    text:str

@app.get("/notes")
def get_notes():
    return read()

@app.post("/notes")
def create_note(data:Notat):
        data = read()
        data.append(data)
        write(data)