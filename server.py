from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from fastapi.middleware.cors import CORSMiddleware

# ── App ──
app = FastAPI(title="Notat API")

# ── CORS ──
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── Database ──
def get_connection():
    return sqlite3.connect("database.db")


with get_connection() as conn:
    conn.cursor().execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            text  TEXT NOT NULL
        )
    """)
    conn.commit()


# ── Datamodell ──
class Notat(BaseModel):
    title: str
    text: str


# ── Endepunkter ──

@app.post("/notat", status_code=201)
def nytt_notat(data: Notat):
    """Opprett et nytt notat."""
    with get_connection() as conn:
        conn.cursor().execute(
            "INSERT INTO notes (title, text) VALUES (?, ?)",
            (data.title, data.text),
        )
        conn.commit()
    return {"message": "Notat lagret"}


@app.get("/notat")
def hent_notater():
    """Hent alle notater."""
    with get_connection() as conn:
        rows = conn.cursor().execute(
            "SELECT id, title, text FROM notes"
        ).fetchall()
    return [{"id": r[0], "title": r[1], "text": r[2]} for r in rows]


@app.get("/notat/{note_id}")
def hent_notat(note_id: int):
    """Hent ett notat på ID."""
    with get_connection() as conn:
        row = conn.cursor().execute(
            "SELECT id, title, text FROM notes WHERE id = ?",
            (note_id,),
        ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Notat ikke funnet")
    return {"id": row[0], "title": row[1], "text": row[2]}


@app.delete("/notat/{note_id}")
def slett_notat(note_id: int):
    """Slett ett notat på ID."""
    with get_connection() as conn:
        row = conn.cursor().execute(
            "SELECT id FROM notes WHERE id = ?", (note_id,)
        ).fetchone()
        if not row:
            raise HTTPException(status_code=404, detail="Notat ikke funnet")
        conn.cursor().execute(
            "DELETE FROM notes WHERE id = ?", (note_id,)
        )
        conn.commit()
    return {"message": "Notat slettet"}