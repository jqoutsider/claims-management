import logging
from flask import Blueprint, request, jsonify, Flask
from services.assignment_service import AssignmentService

user_api = Blueprint('assingment_api', __name__)

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

@user_api.route('/api/assignment', methods=['POST'])
def create_assingment_controller():
    app.logger.info('creating assignment')

    data = request.get_json()
    AssignmentService.create_assignment_service(data)

    return jsonify("User has been successfully created."), 201