from flask import Blueprint, request, jsonify
from app.models import Task, User
from app.database import db

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('/', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([
        {'id': t.id, 'title': t.title, 'description': t.description, 'status': t.status, 'assigned_to': t.assigned_to}
        for t in tasks
    ])

@bp.route('/', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        assigned_to=data.get('assigned_to')
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created', 'id': new_task.id}), 201

@bp.route('/<int:task_id>/status', methods=['PUT'])
def update_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.json
    task.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Task status updated'})
