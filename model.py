from sqlalchemy import Column, Integer, ForeignKey, String, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///nklyga.db")

Base = declarative_base()

team_sponsor_table = Table("team_sponsor", Base.metadata,
    Column("team_id", Integer, ForeignKey("team.id")),
    Column("sponsor_id", Integer, ForeignKey("sponsor.id"))
)

class Player(Base):
    __tablename__ = "player"
    id = Column(Integer, primary_key=True)
    jersey_number = Column("jersey_number", Integer)
    f_name = Column("Name", String)
    l_name = Column("Surname", String)
    age = Column("Age", Integer)
    height = Column("Height", String)
    weight = Column("Weight", String)
    position = Column("Position", String)
    salary = Column("Salary", Integer)
    birth_country = Column("Birth country", String)
    team = relationship("Team", back_populates = "players")
    team_id = Column("team_id", Integer, ForeignKey("team.id"))

    def __repr__(self):
        return f"#{self.jersey_number} | NAME: {self.f_name} | SURNAME: {self.l_name} | AGE: {self.age} | HEIGHT: {self.height} | WEIGHT: {self.weight} | POS: {self.position} | NATIONALITY: {self.birth_country} | SALARY: {self.salary}"


class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    f_name = Column("Name", String)
    l_name = Column("Surname", String)
    responsibility = Column("Responsibility", String)
    salary = Column("Salary", Integer)
    team = relationship("Team", back_populates = "staff_members")
    team_id = Column("team_id", Integer, ForeignKey("team.id"))

    def __repr__(self):
        return f"NAME:{self.f_name} | SURNAME: {self.l_name} | RESPONSIBILITY: {self.responsibility} | SALARY: {self.salary}"


class Team(Base):
    __tablename__ = "team"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    budget = Column("Budget", Integer)
    players = relationship("Player", back_populates = "team")
    staff_members = relationship("Staff", back_populates = "team")
    arena = relationship("Arena", back_populates = "teams")
    arena_id = Column("arena_id", Integer, ForeignKey("arena.id"))
    sponsors = relationship(
        "Sponsor",
        secondary = team_sponsor_table,
        back_populates = "teams"
    )

    def __repr__(self):
        return f"{self.id}, {self.name}, team budget: {self.budget}"


class Arena(Base):
    __tablename__ = "arena"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    address = Column("Address", String)
    capacity = Column("Capacity", Integer)
    teams = relationship("Team", back_populates = "arena")
    

    def __repr__(self):
        return f"HOME COURT: {self.name} | ADDRESS: {self.address} | CAPACITY: {self.capacity}"


class Sponsor(Base):
    __tablename__ = "sponsor"
    id = Column(Integer, primary_key=True)
    name = Column("name", String)
    teams = relationship(
        "Team",
        secondary = team_sponsor_table,
        back_populates = "sponsors"
    )

    def __repr__(self):
        return f"{self.name}"

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)