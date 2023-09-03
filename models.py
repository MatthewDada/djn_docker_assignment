import datetime as _dt
import sqlalchemy as _sql

import database as _database

class SoccerTeam(_database.Base):
    __tablename__ = "teams"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    club_name = _sql.Column(_sql.String, index=True)
    best_player = _sql.Column(_sql.String, index=True)
    shirt_number = _sql.Column(_sql.String, index=True)
    age = _sql.Column(_sql.Integer, index=True)
    date_created = _sql.Column(_sql.DateTime, default=_dt.datetime.utcnow)

