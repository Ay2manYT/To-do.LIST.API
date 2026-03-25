from fastapi import FastAPI
import json, os

app = FastAPI()
FILE = "data.json"

def read():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def write(data):
    json.dump(data, open(FILE, "w"), indent=2)

@app.get("/notes")
def get_notes():
    return read()

@app.post("/notes")
def create_note(note: dict):
    data = read()
    data.append(note)
    write(data)
    return note