from fastapi import FastAPI
from journal import Journal
import journal
from pydantic import BaseModel


app = FastAPI()

journal = Journal()

class EntryRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message":"mindledger api running"}


@app.post("/entry")
def add_entry(payload: EntryRequest):
    entry = journal.add_entry(payload.text)
    return {"entry":entry}

@app.get("/entries/all")
def all_entries():
    entries = journal.fetch_all_entries()
    return {"entries": entries}

@app.get("/entries/latest")
def latest_entries(limit: int = 10):
    entries = journal.fetch_latest(limit)
    return {"entries": entries}

@app.get("/reflect")
def reflect():
    return journal.reflect()













