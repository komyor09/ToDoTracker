import json, os
from models import Task

FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        data = json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(task):
    tasks = load_tasks()
    
        
