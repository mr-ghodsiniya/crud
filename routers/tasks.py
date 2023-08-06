from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from schemas import tasks_s
from models import tasks_m
from dependencies import get_db


router = APIRouter()


@router.post("/tasks/", response_model=tasks_s.TaskInfo)
def create_task(task:tasks_s.CreateTask, db: Session = Depends(get_db)):
    new_task = tasks_m.Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.get("/tasks/")
def all_tasks(db: Session = Depends(get_db)):
    all_task = db.query(tasks_m.Task).all()
    if all_task is None:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return all_task


@router.get("/tasks/{task_id}", response_model=tasks_s.TaskInfo)
def read_task(task_id:int, db: Session = Depends(get_db)):
    task = db.query(tasks_m.Task).filter(tasks_m.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.patch("/tasks/{task_id}", response_model=tasks_s.TaskInfo)
def update_task(task_id: int, n_task:tasks_s.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(tasks_m.Task).filter(tasks_m.Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if n_task.title is None:
        task.title = task.title
    else:
        task.title = n_task.title
    if n_task.description is None:
        task.description = task.description
    else:
        task.description = n_task.description
    db.commit()
    db.refresh(task)
    return task


@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(tasks_m.Task).filter(tasks_m.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return "task deleted"