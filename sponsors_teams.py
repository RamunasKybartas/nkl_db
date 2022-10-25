from model import engine, Team, Sponsor
from sqlalchemy.orm import sessionmaker
from pprint import pprint
session = sessionmaker(bind=engine)()

sponsors = session.query(Sponsor).all()
teams = session.query(Team).all()

j = 0
for team in teams:
    count = 0
    for sponsor in sponsors:
        if count == 3:
                break
        team.sponsors.append(sponsors[j])
        session.commit()
        j += 1
        count += 1






