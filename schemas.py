import datetime as dt
import pydantic as _pydantic

class _BaseTeam(_pydantic.BaseModel):
    club_name: str
    best_player: str
    shirt_number: str
    age: int

class SoccerTeam(_BaseTeam):
    id: int
    date_created: dt.datetime

    class Config:
        # orm_mode = True
        from_attributes = True

class CreateTeam(_BaseTeam):
    pass