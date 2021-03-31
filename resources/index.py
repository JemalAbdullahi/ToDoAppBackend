from flask_restful import Resource


class Index(Resource):

    # A welcome message to test our server
    def index():
        return "<h1>Welcome to our server !!</h1>"
