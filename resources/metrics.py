from flask_restful import Resource, reqparse
from models.metrics import MetricsModel


class Metrics(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument("country", type=str, required=False)
    parser.add_argument("os", type=str, required=False)
    parser.add_argument("channel", type=str, required=False)
    parser.add_argument("date_from", type=str, required=False)
    parser.add_argument("date_to", type=str, required=False)
    parser.add_argument("sort_by", type=str, required=False, default="country")
    parser.add_argument("order", type=str, required=False, default="asc")
    parser.add_argument("group_by", type=str, required=False)

    parser.add_argument("clicks", type=int, required=False)
    parser.add_argument("installs", type=int, required=False)
    parser.add_argument("impressions", type=int, required=False)

    parser.add_argument("spend", type=float, required=False)
    parser.add_argument("revenue", type=float, required=False)

    def get(self):
        data = Metrics.parser.parse_args()
        metrics = MetricsModel(**data).search()
        if metrics:
            return [metric.json() for metric in metrics]
        return {"message": "Metrics not found"}, 404
