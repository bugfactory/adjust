import os

from flask import Flask

from flask_restful import Api
from resources.metrics import Metrics

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "sqlite:///metrics.sqlite3",
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

api.add_resource(Metrics, "/api/v1/metrics")


if __name__ == "__main__":
    from db import db

    db.init_app(app)
    app.run(port=4000, host="0.0.0.0")
