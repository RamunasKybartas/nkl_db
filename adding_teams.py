from model import engine, Team
from sqlalchemy.orm import sessionmaker
import openpyxl

Session = sessionmaker(bind=engine)
session = Session()

wb = openpyxl.load_workbook("teams.xlsx")
ws = wb["teams"]
rows = ws.iter_rows(min_row=2, max_row=15, min_col=1, max_col=3)

for team_name, budget, arena in rows:
    team = Team(name=team_name.value, budget=budget.value, arena_id=arena.value)
    session.add(team)
    session.commit()
   









