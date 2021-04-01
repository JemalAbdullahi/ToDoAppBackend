from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

from api.api import api_bp
app.register_blueprint(api_bp, url_prefix='/api')

from Models import db
db.init_app(app)


@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
