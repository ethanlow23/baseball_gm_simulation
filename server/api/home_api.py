from flask import Blueprint, request, jsonify
from app import db, League, Team, Player, Game

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
    return jsonify({"message": "welcome to baseball gm simulation"})

# TEST ROUTE TO VIEW DATABASE INFORMATION
@home_api.route('/welcome')
def welcome():
    leagues = League.query.all()
    return jsonify([league.serialize() for league in leagues])
@home_api.route('/games')
def games():
    games = Game.query.all()
    game = Game.query.first()
    print(game.teams)
    return jsonify([game.serialize() for game in games])

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
                position = "SP"
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
        for i in range(1, len(teams)):
            teams = teams[:1] + teams[len(teams) - 1:] + teams[1:len(teams) - 1]
            for j in range(int(len(teams) / 2)):
                season = 2020
                game_number = str(i)
                game = Game(season=season, game_number=game_number)
                game.teams.append(teams[j])
                game.teams.append(teams[len(teams) - 1 - j])
                db.session.add(game)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to schedule game"})
        return jsonify({"success": "generated schedule"})

@home_api.route('/simulate', methods=['GET', 'POST'])
def simulate():
    if request.method == 'POST':
        return jsonify({"success": "game completed"})
    else:
        import random

        team_1 = Game.query.first().teams[0]
        team_2 = Game.query.first().teams[1]
        home_lineup = Player.query.filter_by(team_id=team_1.id).filter(Player.first_name != "SP")
        home_pitcher = Player.query.filter_by(team_id=team_1.id).filter(Player.first_name == "SP")[0]
        away_lineup = Player.query.filter_by(team_id=team_2.id).filter(Player.first_name != "SP")
        away_pitcher = Player.query.filter_by(team_id=team_2.id).filter(Player.first_name == "SP")[0]
        # GAME SIMULATION CODE
        # =============================================================================================================================
        away_score = 0
        home_score = 0
        half_inning = 0
        away_outs = 0
        home_outs = 0
        first_base = 0
        second_base = 0
        third_base = 0
        away_plate_appearances = 0
        home_plate_appearances = 0
        away_scoreboard = []
        home_scoreboard = []
        home_box_score = [
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
        ]
        away_box_score = [
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0},
            {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
        ]

        while (away_outs < 27 or away_score == home_score):
            while (half_inning == 0):
                batter = away_lineup[away_plate_appearances % 9]
                away_box_score[away_plate_appearances % 9]["AB"] += 1
                away_plate_appearances += 1
                matchup_multiplier = ((batter.contact - home_pitcher.velocity) / 100) + 1
                pitch = random.randint(0, 1000)
                swing = batter.contact * 3.6 * matchup_multiplier
                if (swing >= pitch):
                    away_box_score[away_plate_appearances % 9]["H"] += 1
                    if (pitch > 0 and pitch < swing * 0.15):
                        print("HOME RUN")
                        away_box_score[away_plate_appearances % 9]["HR"] += 1
                        rbis = first_base + second_base + third_base + 1
                        away_box_score[away_plate_appearances % 9]["RBI"] += rbis
                        away_score += rbis
                        first_base = 0
                        second_base = 0
                        third_base = 0
                    elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                        print("TRIPLE")
                        away_box_score[away_plate_appearances % 9]["3B"] += 1
                        rbis = first_base + second_base + third_base
                        away_box_score[away_plate_appearances % 9]["RBI"] += rbis
                        away_score += rbis
                        first_base = 0
                        second_base = 0
                        third_base = 0
                    elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                        print("DOUBLE")
                        away_box_score[away_plate_appearances % 9]["2B"] += 1
                        rbis = second_base + third_base
                        away_box_score[away_plate_appearances % 9]["RBI"] += rbis
                        away_score += rbis
                        third_base = first_base
                        second_base = 1
                        first_base = 0
                    else:
                        print("SINGLE")
                        rbis = third_base
                        away_score += rbis
                        away_box_score[away_plate_appearances % 9]["RBI"] += rbis
                        third_base = second_base
                        second_base = first_base
                        first_base = 1
                else:
                    print("OUT")
                    away_outs += 1
                    if (away_outs % 3 == 0):
                        half_inning = 1
            first_base = 0
            second_base = 0
            third_base = 0
            print("End of top half of inning...")
            while (half_inning == 1 and (home_outs < 24 or away_score >= home_score)):
                batter = home_lineup[home_plate_appearances % 9]
                home_box_score[home_plate_appearances % 9]["AB"] += 1
                home_plate_appearances += 1
                matchup_multiplier = ((batter.contact - away_pitcher.velocity) / 100) + 1
                pitch = random.randint(0, 1000)
                swing = batter.contact * 3.6 * matchup_multiplier
                if (swing >= pitch):
                    home_box_score[home_plate_appearances % 9]["H"] += 1
                    if (pitch > 0 and pitch < swing * 0.15):
                        print("HOME RUN")
                        home_box_score[home_plate_appearances % 9]["HR"] += 1
                        rbis = first_base + second_base + third_base + 1
                        home_box_score[home_plate_appearances % 9]["RBI"] += rbis
                        home_score += rbis
                        first_base = 0
                        second_base = 0
                        third_base = 0
                    elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                        print("TRIPLE")
                        home_box_score[home_plate_appearances % 9]["3B"] += 1
                        rbis = first_base + second_base + third_base
                        home_box_score[home_plate_appearances % 9]["RBI"] += rbis
                        home_score += rbis
                        first_base = 0
                        second_base = 0
                        third_base = 0
                    elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                        print("DOUBLE")
                        home_box_score[home_plate_appearances % 9]["2B"] += 1
                        rbis = second_base + third_base
                        home_box_score[home_plate_appearances % 9]["RBI"] += rbis
                        home_score += rbis
                        third_base = first_base
                        second_base = 1
                        first_base = 0
                    else:
                        print("SINGLE")
                        rbis = third_base
                        home_score += rbis
                        home_box_score[home_plate_appearances % 9]["RBI"] += rbis
                        third_base = second_base
                        second_base = first_base
                        first_base = 1
                else:
                    print("OUT")
                    home_outs += 1
                    if (home_outs % 3 == 0):
                        half_inning = 0
            first_base = 0
            second_base = 0
            third_base = 0
            print("End of bottom half of inning...")
        print("------------------------")
        print("End of game")
        print("Final score is away " + str(away_score) + "-" + str(home_score) + " home")
        print("------------------------")
        for away_player in away_box_score:
            print(away_player)
        print("------------------------")
        for home_player in home_box_score:
            print(home_player)
        # =============================================================================================================================
        return jsonify(team_1.serialize())
