from model import Player, Arena, Staff, Team, Sponsor, engine
from sqlalchemy.orm import sessionmaker
from pprint import pprint
Session = sessionmaker(bind=engine)
session = Session()



while True:
    print("-" * 10, "NKL DATABASE", "-" * 10)
    choice = int(input("1 - Look all teams\n2 - Look a specific team\n3 - Transfer player or staff member\n4 - Add a new sponsor\n9 - Quit\nChoose: "))
    if choice == 9:
        print("Quittting...")
        break
    if choice == 1:
        teams = session.query(Team).all()
        for team in teams:
            print(team)
    if choice == 2:
        teams = session.query(Team).all()
        for team in teams:
            print(team)
        try:
            team_id = int(input("Enter teams ID to choose: "))
        except ValueError:
            print("Teams ID must be a digit to a maximum of team count")
        else:
            shown_team = session.query(Team).get(team_id)
            print("-" * 15, "PLAYERS OF", shown_team.name.upper(), "-" * 15)
            pprint(shown_team.players)
            print("-" * 15, "STAFF MEMBERS", shown_team.name.upper(), "-" * 15)
            pprint(shown_team.staff_members)
            print("-" * 50)
            print(f"SPONSORS: {shown_team.sponsors}")
            print("-" * 50)
            print(shown_team.arena)
    if choice == 3:
        transfer_choice = int(input("1 - To transfer a player\n2 - To transfer a staff member: "))
        if transfer_choice == 1:
            chosen_players_name = input("Enter name or surname of a player: ")
            shown_player_name = session.query(Player).filter(Player.f_name.ilike(f"%{chosen_players_name}%")).all()
            shown_player_surname = session.query(Player).filter(Player.l_name.ilike(f"%{chosen_players_name}%")).all() 
            for player in shown_player_name:
                print(player.id, player.f_name, player.l_name, player.team.name)
            for player_surname in shown_player_surname:
                print(player_surname.id, player_surname.f_name, player_surname.l_name, player_surname.team.name)
            chosen_id = int(input("Choose players ID: "))
            moved_player = session.query(Player).get(chosen_id)
            teams = session.query(Team).all()
            for team in teams:
                print(team)       
            chosen_team = int(input("Choose Teams ID to move Player to"))
            added_to_team = session.query(Team).get(chosen_team)
            transfered_player = added_to_team.players.append(moved_player)
            session.commit()
            print("Player transfered successfully")
        if transfer_choice == 2:
            chosen_staff_name = input("Enter name or surname of a staff member: ")
            shown_staff_name = session.query(Staff).filter(Staff.f_name.ilike(f"%{chosen_staff_name}%")).all() 
            shown_staff_surname = session.query(Staff).filter(Staff.l_name.ilike(f"%{chosen_staff_name}%")).all() 
            for staff in shown_staff_name:
                print(staff.id, staff.f_name, staff.l_name, staff.team.name)
            for staff_surname in shown_staff_surname:
                print(staff_surname.id, staff_surname.f_name, staff_surname.l_name, staff_surname.team.name)
            chosen_staff_id = int(input("Choose staff members ID: "))
            moved_staff = session.query(Staff).get(chosen_staff_id)
            teams = session.query(Team).all()
            for team in teams:
                print(team)       
            chosen_staffs_team = int(input("Choose Teams ID to move staff member to: "))
            staff_added_to_team = session.query(Team).get(chosen_staffs_team)
            transfered_staff= staff_added_to_team.staff_members.append(moved_staff)
            session.commit()
            print("Staff member transfered successfully")
    if choice == 4:
        teams = session.query(Team).all()
        sponsor_name = input("Enter new sponsors name: ")
        new_sponsor = Sponsor(name=sponsor_name)
        session.add(new_sponsor)
        session.commit()
        print("CHOOSE WHICH TEAM(S) THE SPONSOR WILL BE SPONSORING")
        for team in teams:
                print(team.id, team.name.upper()) 
        while True:
            sponsored_team_id = input("Enter sponsored team ID or Q to finish adding: ")
            if sponsored_team_id.casefold() == "q":
                break
            sponsored_team = session.query(Team).get(int(sponsored_team_id))
            sponsored_team.sponsors.append(new_sponsor)
            session.commit()
            print(f"Sponsor {sponsor_name} to the team {sponsored_team.name} added successfully")

