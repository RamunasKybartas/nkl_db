from model import engine, Sponsor
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

sponsors = ["7bet", "Paskolų klubas", "Topo centras", "Mantinga", 
    "Rokiškio sūris", "Žalia giria", "Autotoja", "Info diena", 
    "Delfi", "Orlen Lietuva", "Vilkyškių pieninė", "ecodenta", 
    "Premia", "Viči", "Zigmo žuvys", "Lidl", "Camelia vaistinė", 
    "Biržų duona", "Džiugas", "Gintarinė vaistinė", "IKI",
    "Swedbank", "Maxima", "Tele2", "Akvilė", "Žemaitijos pienas",
    "Biovela", "Vytautas", "Elektromarkt", "Perlas", "VR Servisas",
    "Akvaservis", "Švyturys", "IKEA", "Vilniaus Universitetas", "Pieno žvaigždės",
    "Vilniaus alus", "Kalnapilis", "TELE2", "Olifėja", "Compensa", "TonyBet", ]


for x in sponsors:
  sponsor = Sponsor(name=x)
  session.add(sponsor)
  session.commit() 

