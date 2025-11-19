from logging import DEBUG
from urllib.parse import quote_plus



from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from todor import todo, auth

password = quote_plus("Sport123!")
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        DEBUG=True,
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://sport_user:Sport123!@localhost:5432/todolist",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)

    # Registro de blueprints
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route("/")
    def index():
        return render_template("index.html")

    #with app.app_context():
        #db.create_all()

    return app
