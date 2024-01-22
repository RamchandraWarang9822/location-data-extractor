from typing import List 

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Samuel Warang", age=22),
    Person(id=2, name="Ramchandra Warang", age=22),
    Person(id=3, name="Aditya Babar", age=25),
    Person(id=4, name="Niveditta Khude", age=23),
    Person(id=5, name="Aditya Babar", age=25),
]

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api")
def read_root():
    return DB 
