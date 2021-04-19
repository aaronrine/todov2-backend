import json
from fastapi import FastAPI, Form, HTTPException
from typing import Optional, List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

#TODO: Link with database
#TODO: add users and userauth

class Todo(BaseModel):
    id: Optional[str] = None
    marked: bool
    text: str
    priority: int

class Todos(BaseModel):
    todos: List[Todo]

class TodoIds(BaseModel):
    todo_ids: List[str]

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],

)

todos = [
    {"id": 'jfkd', "marked": True, "text": "get milk", "priority": 4},
    {"id": 'jfke', "marked": True, "text": "walk dog", "priority": 4},
    {"id": 'jfkf', "marked": True, "text": "create bottle", "priority": 4},
]


def getTodo(id: str):
    for  todo in todos:
        if todo['id'] == id:
            return todo
    raise HTTPException(status_code=404, detail="Item could not be found")


def getTodoIndexById(id: str):
    for i, dic in enumerate(todos):
        if dic["id"] == id:
            return i
    return -1

@app.get("/todos/")
async def list_todos():
    return todos


@app.post("/todos/create/")
async def add_todo(todo: Todo):
    todos.append(todo)
    return {
        "id": todo.id,
        "marked": todo.marked,
        "text": todo.text,
        "priority": todo.priority,
    }


@app.put('/todos/')
async def update_todo(todo: Todo):
    idx = getTodoIndexById(todo.id)
    todos[idx] = {
        "id": todo.id,
        "marked": todo.marked,
        "text": todo.text,
        "priority": todo.priority,
    }
    return {"todo": todos[idx]}


@app.delete('/todos/{id}/')
async def delete_todo(id:str):
    idx = getTodo(id)[1]
    todos.pop(idx)
    return "success"


@app.post('/todos/sort/')
async def sort_todos(todos_ids:TodoIds):
    global todos
    todos = [getTodo(todoId) for todoId in todos_ids.todo_ids]
    return "success"
