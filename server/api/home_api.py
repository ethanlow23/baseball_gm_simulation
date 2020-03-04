from flask import Blueprint, request, jsonify
from app import db, League, Team, Player

home_api = Blueprint('home_api', __name__)

cities = [
    "Arizona", "Atlanta", "Baltimore", "Boston", "Chicago", "Chicago", "Cincinnati", "Cleveland", "Colorado", "Detroit", "Houston", "Kansas City", "Los Angeles", "Los Angeles", "Miami", "Milwaukee", "Minnesota", "New York", "New York", "Oakland", "Philadelphia", "Pittsburgh", "San Diego", "San Francisco", "Seattle", "St. Louis", "Tampa Bay", "Texas", "Toronto", "Washington"
]
positions = [
    "LF", "CF", "RF", "3B", "SS", "2B", "1B", "C", "DH"
]

# HOME SCREEN
@home_api.route('/')
def home():
    return jsonify({"message": "welcome to baseball gm simulation", "user_team": user_team.serialize()})

# TEST ROUTE TO VIEW DATABASE INFORMATION
@home_api.route('/welcome')
def welcome():
    leagues = League.query.all()
    return jsonify([league.serialize() for league in leagues])

# CREATE A LEAGUE, GENERATE TEAMS AND PLAYERS
@home_api.route('/league', methods=['POST'])
def create_league():
    if request.method == 'POST':
        # CREATE A LEAGUE
        leagues_count = League.query.count()
        league_name = "League " + str(leagues_count)
        league = League(name=league_name)
        db.session.add(league)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": "failed to create new league"})
        # GENERATE TEAMS
        for i in range(len(cities)):
            city = cities[i]
            name = "team" + str(i)
            team = Team(city=city, name=name, league=league)
            db.session.add(team)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({"error": "failed to generate team"})
            # GENERATE PLAYERS
            for i in range(len(positions)):
                first_name = positions[i]
                last_name = "Player" + str(i)
                age = 22
                position = positions[i]
                contact = 80
                power = 80
                velocity = 0
                player = Player(first_name=first_name, last_name=last_name, age=age, position=position, contact=contact, power=power, velocity=velocity, league=league, team=team)
                db.session.add(player)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to generate player"})
            for i in range(5):
                first_name = "SP"
                last_name = "Pitcher" + str(i + 1)
                age = 22
                position = positions[i]
                contact = 0
                power = 0
                velocity = 80
                pitcher = Player(first_name=first_name, last_name=last_name, age=age, position=position, contact=contact, power=power, velocity=velocity, league=league, team=team)
                db.session.add(pitcher)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to generate pitcher"})
        return jsonify({"success": "created new league"})

# GENERATE SEASON SCHEDULE
@home_api.route('/schedule', methods=['POST'])
def generate_scheduele():
    if request.method == 'POST':
        teams = Team.query.all()
        for team in teams:
            for matchup in teams:
                if team.id != matchup.id:
                    opponent = matchup.name
                    game = Game(opponent=opponent, team=team)
                    db.session.add(game)
                    try:
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        db.session.rollback()
                        return jsonify({"error": "failed to schedule game"})
        return jsonify({"success": "generated schedule"})
