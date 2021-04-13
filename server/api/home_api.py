from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

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

# CREATE A SEASON, GENERATE TEAMS AND PLAYERS
@home_api.route('/season', methods=['POST'])
def create_league():
    if request.method == 'POST':
        # CREATE A SEASON
        season = Season(year=2021)
        db.session.add(season)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            return jsonify({"error": "failed to create new season"})
        # GENERATE TEAMS
        for i in range(len(cities)):
            city = cities[i]
            name = "team" + str(i)
            team = Team(city=city, name=name, season=season)
            db.session.add(team)
            try:
                db.session.commit()
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
                player = Player(first_name=first_name, last_name=last_name, age=age, position=position, contact=contact, power=power, velocity=velocity, season=season, team=team)
                db.session.add(player)
                try:
                    db.session.commit()
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
                pitcher = Player(first_name=first_name, last_name=last_name, age=age, position=position, contact=contact, power=power, velocity=velocity, season=season, team=team)
                db.session.add(pitcher)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to generate pitcher"})
        return jsonify({"success": "created new season"})

# GENERATE SEASON SCHEDULE
@home_api.route('/schedule', methods=['POST'])
def generate_schedule():
    if request.method == 'POST':
        season = Season.query.get(1)
        teams = season.teams
        for i in range(1, len(teams)):
            teams = teams[:1] + teams[len(teams) - 1:] + teams[1:len(teams) - 1]
            for j in range(int(len(teams) / 2)):
                game_number = str(i)
                game = Game(game_number=game_number, season=season, home=teams[j], away=teams[len(teams) - 1 - j])
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

        # game_number = Game.query.filter(Game.away_score == 0 and Game.home_score == 0).first().game_number
        season = Season.query.get(1)
        game_number = (Game.query.filter(Game.home_team_stat.has()).count() // 15) + 1
        games = Game.query.filter_by(season=season).filter_by(game_number=game_number)
        for game in games:
            home_lineup = Player.query.filter_by(team_id=game.home.id).filter(Player.position != "SP")
            home_pitcher = Player.query.filter_by(team_id=game.home.id).filter(Player.position == "SP")[(game_number - 1) % 5]
            away_lineup = Player.query.filter_by(team_id=game.away.id).filter(Player.position != "SP")
            away_pitcher = Player.query.filter_by(team_id=game.away.id).filter(Player.position == "SP")[(game_number - 1) % 5]
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
                inning += 1
                while (half_inning == 0):
                    result = runs = None
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
                        home_pitching["H"] += 1
                        if (pitch > 0 and pitch < swing * 0.15):
                            print("HOME RUN")
                            result = "HR"
                            home_pitching["HR"] += 1
                            runs = first_base + second_base + third_base + 1
                            first_base = second_base = third_base = 0
                        elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                            print("TRIPLE")
                            result = "3B"
                            runs = first_base + second_base + third_base
                            first_base = second_base = 0
                            third_base = 1
                        elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                            print("DOUBLE")
                            result = "3B"
                            runs = first_base + second_base + third_base
                            third_base = first_base
                            second_base = 1
                            first_base = 0
                        else:
                            print("SINGLE")
                            runs = third_base
                            third_base = second_base
                            second_base = first_base
                            first_base = 1
                        if result:
                            away_team_totals[result] += 1
                            away_box_score[away_plate_appearances % 9][result] += 1
                        away_team_totals["RBI"] += runs
                        away_box_score[away_plate_appearances % 9]["RBI"] += runs
                        home_pitching["R"] += runs
                        away_score += runs
                    else:
                        print("OUT")
                        away_outs += 1
                        if (away_outs % 3 == 0):
                            home_pitching["IP"] += 1
                            half_inning = 1
                first_base = second_base = third_base = 0
                print("End of top of inning " + str(inning))
                while (half_inning == 1 and (home_outs < 24 or away_score >= home_score)):
                    result = runs = None
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
                        away_pitching["H"] += 1
                        if (pitch > 0 and pitch < swing * 0.15):
                            print("HOME RUN")
                            result = "HR"
                            away_pitching["HR"] += 1
                            runs = first_base + second_base + third_base + 1
                            first_base = second_base = third_base = 0
                        elif (pitch > swing * 0.15 and pitch < (swing * 0.15) + (swing * 0.02)):
                            print("TRIPLE")
                            result = "3B"
                            runs = first_base + second_base + third_base
                            first_base = second_base = 0
                            third_base = 1
                        elif (pitch > (swing * 0.15) + (swing * 0.02) and pitch < (swing * 0.15) + (swing * 0.02) + (swing * 0.22)):
                            print("DOUBLE")
                            result = "2B"
                            runs = second_base + third_base
                            third_base = first_base
                            second_base = 1
                            first_base = 0
                        else:
                            print("SINGLE")
                            runs = third_base
                            third_base = second_base
                            second_base = first_base
                            first_base = 1
                        if result:
                            home_team_totals[result] += 1
                            home_box_score[home_plate_appearances % 9][result] += 1
                        home_team_totals["RBI"] += runs
                        home_box_score[home_plate_appearances % 9]["RBI"] += runs
                        away_pitching["R"] += runs
                        home_score += runs
                    else:
                        print("OUT")
                        home_outs += 1
                        if (home_outs % 3 == 0):
                            away_pitching["IP"] += 1
                            half_inning = 0
                first_base = second_base = third_base = 0
                print("End of inning " + str(inning))
            print("------------------------")
            print("End of game")
            print("Final score is away " + str(away_score) + "-" + str(home_score) + " home")
            print("------------------------")
            print(away_team_totals)
            print(home_team_totals)
            print("------------------------")
            for away_player in away_box_score:
                print(away_player)
            print("------------------------")
            for home_player in home_box_score:
                print(home_player)
            print("------------------------")
            print(away_pitching)
            print(home_pitching)
            # =============================================================================================================================
            team_stat = Team_Stat(at_bats=away_team_totals["AB"], hits=away_team_totals["H"], doubles=away_team_totals["2B"], triples=away_team_totals["3B"], homeruns=away_team_totals["HR"], rbi=away_team_totals["RBI"], team=game.away, game=game, season=season)
            db.session.add(team_stat)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({"error": "failed to update team stats"})
            team_stat = Team_Stat(at_bats=home_team_totals["AB"], hits=home_team_totals["H"], doubles=home_team_totals["2B"], triples=home_team_totals["3B"], homeruns=home_team_totals["HR"], rbi=home_team_totals["RBI"], team=game.home, game=game, season=season)
            db.session.add(team_stat)
            try:
                db.session.commit()
            except Exception as e:
                print(e)
                db.session.rollback()
                return jsonify({"error": "failed to update team stats"})
            for i in range(away_lineup.count()):
                player_ab = away_box_score[i]["AB"]
                player_h = away_box_score[i]["H"]
                player_2b = away_box_score[i]["2B"]
                player_3b = away_box_score[i]["3B"]
                player_hr = away_box_score[i]["HR"]
                player_rbi = away_box_score[i]["RBI"]
                player_stat = Player_Stat(at_bats=player_ab, hits=player_h, doubles=player_2b, triples=player_3b, homeruns=player_hr, rbi=player_rbi, player=away_lineup[i], game=game, season=season)
                db.session.add(player_stat)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to update player stats"})
            for i in range(home_lineup.count()):
                player_ab = home_box_score[i]["AB"]
                player_h = home_box_score[i]["H"]
                player_2b = home_box_score[i]["2B"]
                player_3b = home_box_score[i]["3B"]
                player_hr = home_box_score[i]["HR"]
                player_rbi = home_box_score[i]["RBI"]
                player_stat = Player_Stat(at_bats=player_ab, hits=player_h, doubles=player_2b, triples=player_3b, homeruns=player_hr, rbi=player_rbi, player=home_lineup[i], game=game, season=season)
                db.session.add(player_stat)
                try:
                    db.session.commit()
                except Exception as e:
                    print(e)
                    db.session.rollback()
                    return jsonify({"error": "failed to update player stats"})
        return jsonify({"success": "games completed"})
