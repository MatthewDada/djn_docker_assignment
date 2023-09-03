from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas
import sqlalchemy.orm as _orm

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

def add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db 
    finally:
        db.close()

async def create_team(team: _schemas.CreateTeam, db: "Session") -> _schemas.SoccerTeam:
    team = _models.SoccerTeam(**team.dict())
    db.add(team)
    db.commit()
    db.refresh(team)
    return _schemas.SoccerTeam.model_validate(team)

async def get_all_teams(db:"Session") -> List[_schemas.SoccerTeam]:
    teams = db.query(_models.SoccerTeam).all()
    return list(map(_schemas.SoccerTeam.model_validate, teams)) 

async def get_teams(team_id: int, db: "Session"):
    team = db.query(_models.SoccerTeam).filter(_models.SoccerTeam.id == team_id).first()
    return team
     
async def delete_team(team: _models.SoccerTeam, db: "Session"):
    db.delete(team)
    db.commit()

async def update_team(team_data: _schemas.CreateTeam, team: _models.SoccerTeam, db: "Session") -> _schemas.SoccerTeam:
    team.club_name = team_data.club_name
    team.best_player = team_data.best_player
    team.shirt_number = team_data.shirt_number
    team.age = team_data.age

    db.commit()
    db.refresh(team)

    return _schemas.SoccerTeam.model_validate(team)
    