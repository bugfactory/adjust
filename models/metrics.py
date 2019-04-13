from db import db
from sqlalchemy import func


class MetricsModel(db.Model):

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80))
    channel = db.Column(db.String(80))
    country = db.Column(db.String(80))
    os = db.Column(db.String(80))
    impressions = db.Column(db.Integer)
    clicks = db.Column(db.Integer)
    installs = db.Column(db.Integer)
    spend = db.Column(db.REAL)
    revenue = db.Column(db.REAL)

    def __init__(self, **kwargs):
        self.filters = dict((k, v) for k, v in kwargs.items() if v)

    def json(self):
        return {
            "id": self.id,
            "date": self.date,
            "channel": self.channel,
            "country": self.country,
            "os": self.os,
            "impressions": self.impressions,
            "clicks": self.clicks,
            "installs": self.installs,
            "spend": self.spend,
            "revenue": self.revenue,
        }

    def _add_filter_date_from(self, value, column="date"):
        return func.lower(getattr(MetricsModel, column)) >= func.lower(value)

    def _add_filter_date_to(self, value, column="date"):
        return func.lower(getattr(MetricsModel, column)) <= func.lower(value)

    def _add_filter_generic(self, value, attr):
        return func.lower(getattr(MetricsModel, attr)) == func.lower(value)

    def _add_filter(self, filters, attr, value):
        if attr == "date_from":
            filters.append(self._add_filter_date_from(value))
        elif attr == "date_to":
            filters.append(self._add_filter_date_to(value))
        elif attr == "sort_by" or attr == "order" or attr == "group_by":
            pass
        else:
            filters.append(self._add_filter_generic(value, attr))

    def _sort_by(self, query):
        column = self.filters["sort_by"]
        order = self.filters["order"]
        if order == "desc":
            return query.order_by(getattr(MetricsModel, column).desc())

        return query.order_by(getattr(MetricsModel, column).asc())

    def _group_by(self, query):
        try:
            groups = self.filters.get("group_by", None).split(",")
            for group in groups:
                query = query.group_by(getattr(MetricsModel, group))
        except AttributeError:
            return query

        return query

    def search(self):
        query = db.session.query(MetricsModel)
        filters = []
        for attr, value in self.filters.items():
            self._add_filter(filters, attr, value)
        query = query.filter(*filters)
        query = self._sort_by(query)
        query = self._group_by(query)

        return query.all()
