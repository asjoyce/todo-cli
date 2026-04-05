import json, os, sys
from datetime import date

TASKS_FILE = "tasks.json"

def load():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE) as f:
        return json.load(f)

def save(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add(title):
    tasks = load()
    tasks.append({"id": len(tasks)+1, "title": title, "done": False})
    save(tasks)
    print(f"Added: {title}")

def list_tasks():
    tasks = load()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        status = "✓" if t["done"] else "○"
        print(f"[{status}] {t['id']}. {t['title']}")

def done(task_id):
    tasks = load()
    if not tasks:
        print("No tasks found.")
        return
    for t in tasks:
        if t["id"] == int(task_id):
            t["done"] = True
    save(tasks)

def delete(task_id):
    tasks = load()
    tasks = [t for t in tasks if t["id"] != int(task_id)]
    save(tasks)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "add":    add(sys.argv[2])
    elif cmd == "list": list_tasks()
    elif cmd == "done": done(sys.argv[2])
    elif cmd == "delete": delete(sys.argv[2])