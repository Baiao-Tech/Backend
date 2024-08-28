from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from datetime import date, time

app = FastAPI()

# Modelo de dados para o evento
class Event(BaseModel):
    id: int
    title: str
    date: date
    time: time
    description: Optional[str] = None
    organizers: List[str]
    location: str
    url: Optional[HttpUrl] = None

# Simulação de banco de dados em memória para eventos
events = []

# Rota para obter todos os eventos
@app.get("/events/", response_model=List[Event])
def get_events():
    return events

# Rota para criar um novo evento
@app.post("/events/", response_model=Event)
def create_event(event: Event):
    events.append(event)
    return event

# Rota para obter um evento específico pelo ID
@app.get("/events/{event_id}", response_model=Event)
def get_event(event_id: int):
    for event in events:
        if event.id == event_id:
            return event
    raise HTTPException(status_code=404, detail="Event not found")

# Rota para atualizar um evento
@app.put("/events/{event_id}", response_model=Event)
def update_event(event_id: int, updated_event: Event):
    for index, event in enumerate(events):
        if event.id == event_id:
            events[index] = updated_event
            return updated_event
    raise HTTPException(status_code=404, detail="Event not found")

# Rota para deletar um evento
@app.delete("/events/{event_id}", response_model=Event)
def delete_event(event_id: int):
    for index, event in enumerate(events):
        if event.id == event_id:
            return events.pop(index)
    raise HTTPException(status_code=404, detail="Event not found")