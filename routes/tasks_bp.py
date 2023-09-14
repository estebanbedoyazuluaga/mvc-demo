from flask import Blueprint
import controllers.task_controller as controller

bp = Blueprint('tasks', __name__)

bp.route('/index', methods=['GET'])(controller.show_index)

bp.route('/', methods=['GET'])(controller.get_tasks)
bp.route('/', methods=['POST'])(controller.create_task)
bp.route('/<int:task_id>', methods=['GET'])(controller.get_task)
bp.route('/<int:task_id>', methods=['DELETE'])(controller.delete_task)

