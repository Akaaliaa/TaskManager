from flask import Flask, jsonify
from app.database import db
from app.routes import users, tasks

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/taskmanager'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Home Page
    @app.route('/')
    def home():
        return jsonify({
            "message": "Task Manager API is running!",
            "endpoints": [
                "/users/ - Manage users",
                "/tasks/ - Manage tasks"
            ]
        })

    # Saving Blueprints
    app.register_blueprint(users.bp)
    app.register_blueprint(tasks.bp)

    with app.app_context():
        db.create_all()

    return app
