from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Tasks API")


class TaskInput(BaseModel):
    title: str
    completed: bool = False


class Task(TaskInput):
    id: int


tasks: list[Task] = []
next_task_id = 1


@app.get("/health")
def health_check():
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    global next_task_id
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    pass