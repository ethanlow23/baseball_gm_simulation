home_lineup = [
    {"position": "LF", "contact": 86, "power": 70},
    {"position": "CF", "contact": 79, "power": 70},
    {"position": "RF", "contact": 88, "power": 70},
    {"position": "3B", "contact": 89, "power": 70},
    {"position": "SS", "contact": 77, "power": 70},
    {"position": "2B", "contact": 71, "power": 70},
    {"position": "1B", "contact": 69, "power": 70},
    {"position": "C", "contact": 71, "power": 70},
    {"position": "DH", "contact": 75, "power": 70}
]
home_pitcher = {"position": "P", "rating": 89}
away_lineup = [
    {"position": "LF", "contact": 92, "power": 70},
    {"position": "CF", "contact": 83, "power": 70},
    {"position": "RF", "contact": 92, "power": 70},
    {"position": "3B", "contact": 89, "power": 70},
    {"position": "SS", "contact": 83, "power": 70},
    {"position": "2B", "contact": 77, "power": 70},
    {"position": "1B", "contact": 71, "power": 70},
    {"position": "C", "contact": 74, "power": 70},
    {"position": "DH", "contact": 77, "power": 70}
]
away_pitcher = {"position": "P", "rating": 78}

import random

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
        matchup_multiplier = ((batter["contact"] - home_pitcher["rating"]) / 100) + 1
        pitch = random.randint(0, 1000)
        swing = batter["contact"] * 3.6 * matchup_multiplier
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
        matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
        pitch = random.randint(0, 1000)
        swing = batter["contact"] * 3.6 * matchup_multiplier
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