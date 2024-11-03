from models.assignment import Assignment, db

class AssingmentRepository:

    @staticmethod
    def create_assignment_repository(claimId, operatorId, designedDate, processedDate):

        assignment = Assignment(claimId=claimId, operatorId=operatorId, designedDate=designedDate, processedDate=processedDate)
        
        db.session.add(assignment)
        db.session.commit()

        return assignment