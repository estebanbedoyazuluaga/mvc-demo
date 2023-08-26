from flask import Blueprint
from controllers import TaskController

bp = Blueprint('/tasks', __name__)

# bp.route('/', methods=['GET'])(TaskController.show)
bp.route('/',methods=['GET'])(TaskController.get_tasks)
bp.route('/',methods=['POST'])(TaskController.create_task)
bp.route('/<int:task_id>',methods=['GET'])(TaskController.get_task)
bp.route('/<int:task_id>', methods=['DELETE'])(TaskController.delete_task)

