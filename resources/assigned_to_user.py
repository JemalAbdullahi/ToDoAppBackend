from flask_restful import Resource
from flask import request
from Models import db, SubTask, Task, User

class AssignedToUser(Resource):

    # Delete Members: Also, delete Member's tasks related to the specified Group
    def delete(self):
        header = request.headers["Authorization"]
        username = request.args.get('username')

        if not header:
            return {"Messege": "No subtask key!"}, 401
        if not username:
            return {'Message': 'No username provided'}, 400
        else:
            subtask = SubTask.query.filter_by(subtask_key=header).first()
            if subtask:

                for m in subtask.assigned_to_user:
                    if m.username == username:
                        result = User.serialize(m)
                        subtask.assigned_to_user.remove(m)
                        db.session.commit()
                        return {"status": 'success', "data": result}, 200
                return {"status": "Subtask not assigned to User"}, 404
            else:
                return {"status": "Subtask Not Found"}, 404