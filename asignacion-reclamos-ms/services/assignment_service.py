from datetime import datetime
import logging
from flask import Flask
from repositories.assignment_repository import AssingmentRepository

app = Flask(__name__)
app.logger.setLevel(logging.INFO)

class AssignmentService:
    
    @staticmethod
    def create_assignment_service(data):
        claimId = data['claimId']
        operatorId = data['operatorId']
        date_str = data['designedDate']
        designedDate = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_str = data['processedDate']
        processedDate = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%fZ')

        return AssingmentRepository.create_assignment_repository(claimId, operatorId, designedDate, processedDate)