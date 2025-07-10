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

def add_task(title):
    tasks = load_tasks()
    new_id = max([t['id'] for t in tasks], default = 0) + 1
    task = Task(id=new_id, title=title)
    task.append(task.__dict__)
    save_tasks(tasks)
    print(f"✅ Добавлено: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Пока задач нет.")
    for t in tasks:
        status = "✅" if ['is_done'] else "🕒"
        print(f"{t['id']}. {status} {t['title']} (cоздано: {t['created_at']})")
        
    
