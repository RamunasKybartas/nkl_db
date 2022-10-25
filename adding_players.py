from model import engine, Player
from sqlalchemy.orm import sessionmaker
import openpyxl
from random import randint

Session = sessionmaker(bind=engine)
session = Session()

wb = openpyxl.load_workbook("teams.xlsx")
ws = wb["players"]
rows = ws.iter_rows(min_row=2, max_row=172, min_col=1, max_col=8)

for number, full_name, position, height, weight, age, country, team_id in rows:
    name = full_name.value.split()[0]
    surname = full_name.value.split()[1] 
    player = Player(jersey_number=number.value, f_name=name, l_name=surname, position=position.value, 
    height=height.value, weight=weight.value, age=age.value, birth_country=country.value, team_id=team_id.value, salary=randint(3000, 50000))
    session.add(player)
    session.commit()