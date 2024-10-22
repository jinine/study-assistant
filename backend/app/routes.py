from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from app.models import db, User, StudyMaterial, StudyProgress, Quiz, QuizQuestion, StudyNotification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/smart-study'
db.init_app(app)

def register_routes(app: Flask):
    # User Routes
    @app.route('/api/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return jsonify(user.to_dict()), 201

    @app.route('/api/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        user = User.query.get_or_404(user_id)
        return jsonify(user.to_dict())

    @app.route('/api/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict())

    @app.route('/api/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 204

    # Study Material Routes
    @app.route('/api/study_materials', methods=['POST'])
    def create_study_material():
        data = request.get_json()
        material = StudyMaterial(**data)
        db.session.add(material)
        db.session.commit()
        return jsonify(material.to_dict()), 201

    @app.route('/api/study_materials', methods=['GET'])
    def get_all_study_materials():
        materials = StudyMaterial.query.all()
        return jsonify([material.to_dict() for material in materials])

    @app.route('/api/study_materials/<int:material_id>', methods=['GET'])
    def get_study_material(material_id):
        material = StudyMaterial.query.get_or_404(material_id)
        return jsonify(material.to_dict())

    @app.route('/api/study_materials/<int:material_id>', methods=['PUT'])
    def update_study_material(material_id):
        material = StudyMaterial.query.get_or_404(material_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(material, key, value)
        db.session.commit()
        return jsonify(material.to_dict())

    @app.route('/api/study_materials/<int:material_id>', methods=['DELETE'])
    def delete_study_material(material_id):
        material = StudyMaterial.query.get_or_404(material_id)
        db.session.delete(material)
        db.session.commit()
        return jsonify({"message": "Study material deleted"}), 204

    # Study Progress Routes
    @app.route('/api/study_progress', methods=['POST'])
    def create_study_progress():
        data = request.get_json()
        progress = StudyProgress(**data)
        db.session.add(progress)
        db.session.commit()
        return jsonify(progress.to_dict()), 201

    @app.route('/api/study_progress/user/<int:user_id>', methods=['GET'])
    def get_study_progress_by_user(user_id):
        progress = StudyProgress.query.filter_by(user_id=user_id).all()
        return jsonify([p.to_dict() for p in progress])

    # Quiz Routes
    @app.route('/api/quizzes', methods=['POST'])
    def create_quiz():
        data = request.get_json()
        quiz = Quiz(**data)
        db.session.add(quiz)
        db.session.commit()
        return jsonify(quiz.to_dict()), 201

    @app.route('/api/quizzes/material/<int:material_id>', methods=['GET'])
    def get_quizzes_for_material(material_id):
        quizzes = Quiz.query.filter_by(study_material_id=material_id).all()
        return jsonify([quiz.to_dict() for quiz in quizzes])

    @app.route('/api/quizzes/<int:quiz_id>', methods=['GET'])
    def get_quiz(quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        return jsonify(quiz.to_dict())

    @app.route('/api/quizzes/<int:quiz_id>/questions', methods=['POST'])
    def add_question_to_quiz(quiz_id):
        quiz = Quiz.query.get_or_404(quiz_id)
        data = request.get_json()
        question = QuizQuestion(quiz_id=quiz.id, **data)
        db.session.add(question)
        db.session.commit()
        return jsonify(question.to_dict()), 201

    # Study Notification Routes
    @app.route('/api/study_notifications', methods=['POST'])
    def create_study_notification():
        data = request.get_json()
        notification = StudyNotification(**data)
        db.session.add(notification)
        db.session.commit()
        return jsonify(notification.to_dict()), 201

    @app.route('/api/study_notifications/user/<int:user_id>', methods=['GET'])
    def get_notifications_for_user(user_id):
        notifications = StudyNotification.query.filter_by(user_id=user_id).all()
        return jsonify([n.to_dict() for n in notifications])

    if __name__ == '__main__':
        app.run(debug=True)
