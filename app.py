from api import api_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True)
