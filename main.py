from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm

import schemas as _schemas
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session 

app = _fastapi.FastAPI()

@app.post("/api/teams/", response_model = _schemas.SoccerTeam)
async def create_team(team: _schemas.CreateTeam, db: _orm.Session = _fastapi.Depends(_services.get_db) ):
    return await _services.create_team(team=team, db=db)

@app.get("/api/teams/", response_model=List[_schemas.SoccerTeam])
async def get_teams(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_teams(db=db)

@app.get("/api/teams/{team_id}/", response_model=_schemas.SoccerTeam)
async def get_team(team_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    team = await _services.get_teams(db=db, team_id=team_id)
    if team is None:
        raise _fastapi.HTTPException(status_code=404, detail="Team with id does not exist")
    
    return team

@app.delete("/api/teams/{team_id}/")
async def delete_contact(team_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    team = await _services.get_teams(db=db, team_id =team_id)
    if team is None:
        raise _fastapi.HTTPException(status_code=404, detail="Team with id does not exist")
    
    await _services.delete_team(team, db=db)
    return "Successfully deleted the team"

@app.put("/api/teams/{team_id}/", response_model= _schemas.SoccerTeam)
async def update_team(team_id: int, team_data: _schemas.CreateTeam, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    team = await _services.get_teams(db=db, team_id=team_id)
    if team is None:
        raise _fastapi.HTTPException(status_code=404, detail="Team with id does not exist.")
    
    
    return await _services.update_team(team_data=team_data, team=team, db=db)
