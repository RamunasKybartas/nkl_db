from model import engine, Staff
from sqlalchemy.orm import sessionmaker
import openpyxl
from random import randint

Session = sessionmaker(bind=engine)
session = Session()

wb = openpyxl.load_workbook("teams.xlsx")
ws = wb["players"]

rows = ws.iter_rows(min_row=2, max_row=88, min_col=11, max_col=13)

for full_name, responsibility, team_id in rows:
    name = full_name.value.split()[0]
    surname = full_name.value.split()[1]
    staff = Staff(f_name=name, l_name=surname, responsibility=responsibility.value, salary=randint(10000, 60000), team_id=team_id.value)
    session.add(staff)
    session.commit()