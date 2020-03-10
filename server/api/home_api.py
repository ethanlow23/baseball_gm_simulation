from flask import Blueprint, request, jsonify
from app import db, League, Team, Player, Game, Team_Stat, Player_Stat

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
                team_stat = Team_Stat(season=2020, team=team)
                db.session.add(team_stat)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to add team stat"})
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({"error": "failed to generate team"})
            # GENERATE POSITION PLAYERS
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
                    player_stat = Player_Stat(season=2020, player=player)
                    db.session.add(player_stat)
                    try:
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        db.session.rollback()
                        return jsonify({"error": "failed to add player stat"})
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to generate player"})
            # GENERATE PITCHERS
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
                    player_stat = Player_Stat(season=2020, player=pitcher)
                    db.session.add(player_stat)
                    try:
                        db.session.commit()
                    except Exception as e:
                        print(e)
                        db.session.rollback()
                        return jsonify({"error": "failed to add team stat"})
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to generate pitcher"})
        return jsonify({"success": "created new league"})

@home_api.route('/teams')
def teams():
    all_teams = Team.query.all()
    return jsonify([team.serialize() for team in all_teams])

# GENERATE SEASON SCHEDULE
@home_api.route('/schedule', methods=['POST'])
def generate_schedule():
    if request.method == 'POST':
        teams = League.query.get(3).teams
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

@home_api.route('/simulate', methods=['POST'])
def simulate():
    if request.method == 'POST':
        import random

        game_number = Game.query.filter(Game.away_score == 0 and Game.home_score == 0).first().game_number
        games = Game.query.filter_by(game_number=game_number)
        for game in games:
            team_1 = game.teams[0]
            team_2 = game.teams[1]
            home_lineup = Player.query.filter_by(team_id=team_1.id).filter(Player.position != "SP")
            home_pitcher = Player.query.filter_by(team_id=team_1.id).filter(Player.position == "SP")[0]
            away_lineup = Player.query.filter_by(team_id=team_2.id).filter(Player.position != "SP")
            away_pitcher = Player.query.filter_by(team_id=team_2.id).filter(Player.position == "SP")[0]
            # GAME SIMULATION CODE
            # =============================================================================================================================
            away_score = home_score = half_inning = inning = away_outs = home_outs = first_base = second_base = third_base = away_plate_appearances = home_plate_appearances = 0
            away_team_totals = {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
            home_team_totals = {"AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
            away_box_score = []
            away_pitching = {"player": away_pitcher.first_name + " " + away_pitcher.last_name, "IP": 0, "H": 0, "R": 0, "ERA": 0, "HR": 0, "K": 0}
            home_box_score = []
            home_pitching = {"player": home_pitcher.first_name + " " + home_pitcher.last_name, "IP": 0, "H": 0, "R": 0, "ERA": 0, "HR": 0, "K": 0}
            for away_player in away_lineup:
                position_player = away_player.first_name + " " + away_player.last_name
                box_score = {"player": position_player, "AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
                away_box_score.append(box_score)
            for home_player in home_lineup:
                position_player = home_player.first_name + " " + home_player.last_name
                box_score = {"player": position_player, "AB": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0}
                home_box_score.append(box_score)

            while (away_outs < 27 or away_score == home_score):
                inning += 1;
                while (half_inning == 0):
                    batter = away_lineup[away_plate_appearances % 9]
                    away_team_totals["AB"] += 1
                    away_box_score[away_plate_appearances % 9]["AB"] += 1
                    away_plate_appearances += 1
                    matchup_multiplier = ((batter.contact - home_pitcher.velocity) / 100) + 1
                    pitch = random.randint(0, 1000)
                    swing = batter.contact * 3.6 * matchup_multiplier
                    if (swing >= pitch):
                        away_team_totals["H"] += 1
                        away_box_score[away_plate_appearances % 9]["H"] += 1
                        if (pitch > 0 and pitch < swing * 0.15):
                            print("HOME RUN")
                            away_team_totals["HR"] += 1
                            away_box_score[away_plate_appearances % 9]["HR"] += 1
                            rbi = first_base + second_base + third_base + 1
                            away_team_totals["RBI"] += rbi
                            away_box_score[away_plate_appearances % 9]["RBI"] += rbi
                            away_score += rbi
                            first_base = 0
                            second_base = 0
                            third_base = 0
                        elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                            print("TRIPLE")
                            away_team_totals["3B"] += 1
                            away_box_score[away_plate_appearances % 9]["3B"] += 1
                            rbi = first_base + second_base + third_base
                            away_team_totals["RBI"] += rbi
                            away_box_score[away_plate_appearances % 9]["RBI"] += rbi
                            away_score += rbi
                            first_base = 0
                            second_base = 0
                            third_base = 0
                        elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                            print("DOUBLE")
                            away_team_totals["2B"] += 1
                            away_box_score[away_plate_appearances % 9]["2B"] += 1
                            rbi = second_base + third_base
                            away_team_totals["RBI"] += rbi
                            away_box_score[away_plate_appearances % 9]["RBI"] += rbi
                            away_score += rbi
                            third_base = first_base
                            second_base = 1
                            first_base = 0
                        else:
                            print("SINGLE")
                            rbi = third_base
                            away_score += rbi
                            away_team_totals["RBI"] += rbi
                            away_box_score[away_plate_appearances % 9]["RBI"] += rbi
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
                print("End of top of inning " + str(inning))
                while (half_inning == 1 and (home_outs < 24 or away_score >= home_score)):
                    batter = home_lineup[home_plate_appearances % 9]
                    home_team_totals["AB"] += 1
                    home_box_score[home_plate_appearances % 9]["AB"] += 1
                    home_plate_appearances += 1
                    matchup_multiplier = ((batter.contact - away_pitcher.velocity) / 100) + 1
                    pitch = random.randint(0, 1000)
                    swing = batter.contact * 3.6 * matchup_multiplier
                    if (swing >= pitch):
                        home_team_totals["H"] += 1
                        home_box_score[home_plate_appearances % 9]["H"] += 1
                        if (pitch > 0 and pitch < swing * 0.15):
                            print("HOME RUN")
                            home_box_score[home_plate_appearances % 9]["HR"] += 1
                            rbi = first_base + second_base + third_base + 1
                            home_box_score[home_plate_appearances % 9]["RBI"] += rbi
                            home_score += rbi
                            first_base = 0
                            second_base = 0
                            third_base = 0
                        elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                            print("TRIPLE")
                            home_box_score[home_plate_appearances % 9]["3B"] += 1
                            rbi = first_base + second_base + third_base
                            home_box_score[home_plate_appearances % 9]["RBI"] += rbi
                            home_score += rbi
                            first_base = 0
                            second_base = 0
                            third_base = 0
                        elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                            print("DOUBLE")
                            home_box_score[home_plate_appearances % 9]["2B"] += 1
                            rbi = second_base + third_base
                            home_box_score[home_plate_appearances % 9]["RBI"] += rbi
                            home_score += rbi
                            third_base = first_base
                            second_base = 1
                            first_base = 0
                        else:
                            print("SINGLE")
                            rbi = third_base
                            home_score += rbi
                            home_box_score[home_plate_appearances % 9]["RBI"] += rbi
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
                print("End of inning " + str(inning))
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
            for i in range(away_lineup.count()):
                player_stat = Player_Stat.query.filter_by(player_id=away_lineup[i].id).filter_by(season=2020).first()
                player_stat.at_bats = away_box_score[i]["AB"]
                player_stat.hits = away_box_score[i]["H"]
                player_stat.doubles = away_box_score[i]["2B"]
                player_stat.triples = away_box_score[i]["3B"]
                player_stat.homeruns = away_box_score[i]["HR"]
                player_stat.rbi = away_box_score[i]["RBI"]
                db.session.add(player_stat)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    return jsonify({"error": "failed to update player stats"})
            for i in range(home_lineup.count()):
                player_stat = Player_Stat.query.filter_by(player_id=home_lineup[i].id).filter_by(season=2020).first()
                player_stat.at_bats += home_box_score[i]["AB"]
                player_stat.hits += home_box_score[i]["H"]
                player_stat.doubles += home_box_score[i]["2B"]
                player_stat.triples += home_box_score[i]["3B"]
                player_stat.homeruns += home_box_score[i]["HR"]
                player_stat.rbi += home_box_score[i]["RBI"]
                db.session.add(player_stat)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    return jsonify({"error": "failed to update player stats"})
        return jsonify({"success": "games completed"})
