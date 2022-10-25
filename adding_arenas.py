from model import engine, Arena
from sqlalchemy.orm import sessionmaker
import openpyxl

Session = sessionmaker(bind=engine)
session = Session()

wb = openpyxl.load_workbook("teams.xlsx")
ws = wb["arenas"]

rows = ws.iter_rows(min_row=2, max_row=14, min_col=1, max_col=3)

for arena_name, address, capacity in rows:
    arena = Arena(name=arena_name.value, address=address.value, capacity=capacity.value)
    session.add(arena)
    session.commit()

