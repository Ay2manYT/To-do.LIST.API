from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# 1. Lag app først
app = FastAPI(title="Sitat App")

# 2. Så legg til CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
def get_connection():
    return sqlite3.connect("database.db")

# Lag tabell hvis den ikke finnes
with get_connection() as conn:
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        text TEXT NOT NULL
    )
    """)
    conn.commit()

# Data modell
class Notat(BaseModel):
    title: str
    text: str

# POST - lag notat
@app.post("/notat")
def nytt_notat(data: Notat):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (title, text) VALUES (?, ?)",
            (data.title, data.text)
        )
        conn.commit()
    return {"message": "Notat lagret"}

# GET - hent alle notater
@app.get("/notat")
def hent_notater():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, title, text FROM notes")
        rows = cur.fetchall()
        return [
            {"id": r[0], "title": r[1], "text": r[2]}
            for r in rows
        ]

# GET  hent ett notat
@app.get("/notat/{note_id}")
def hent_notat(note_id: int):
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT id, title, text FROM notes WHERE id = ?",
            (note_id,)
        )
        row = cur.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Not found")
        return {"id": row[0], "title": row[1], "text": row[2]}