from fastapi import FastAPI
import json, os

app = FastAPI()
FILE = "todos.json"

def read():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE))

def write(data):
    json.dump(data, open(FILE, "w"), indent=2)

@app.get("/todos")
def get_todos():
    return read()

@app.post("/todos")
def create(todo: dict):
    data = read()
    todo["id"] = len(data) + 1
    todo["tasks"] = []
    data.append(todo)
    write(data)
    return todo
