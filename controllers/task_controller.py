from flask import jsonify, request, render_template
from models.Task import Task
from models.tasks_db import TasksDB

tasks_db = TasksDB()

def show_index():
    return render_template('index.html')

def get_task(task_id):
    task = tasks_db.get_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    else :
        return jsonify(task.__dict__), 200

def get_tasks():
    # grab all tasks from db, then make a list of dicts
    tasks = [t.__dict__ for t in tasks_db.get_all_tasks()]
    return jsonify(tasks), 200

def create_task():
    data = request.get_json()
    task = Task(
        data['task_id'], 
        data['title'], 
        data['description']
    )
    tasks_db.add_task(task)
    return jsonify(task.__dict__), 201

def delete_task(task_id):
    task = tasks_db.delete_task(task_id)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task.__dict__), 200
