from flask import jsonify, request, render_template
from models.Task import Task, TasksDB

def show():
    return render_template('index.html')

def get_task():
    id = request.get_json()[task_id]
    task = TasksDB.get_task(id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    else :
        return jsonify(task.__dict__)

def get_tasks():
    # grab all tasks from db, then make a list of dicts
    tasks = [t.__dict__ for t in TasksDB.get_all_tasks()]
    return jsonify(tasks)

def create_task():
    data = request.get_json()
    task = Task(data['id'], data['title'], data['description'])
    TasksDB.add_task(task)
    return jsonify(task.__dict__), 201

def delete_task():
    id = request.get_json()[task_id]
    task = TasksDB(id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({"success": "Task deleted successfully"})
