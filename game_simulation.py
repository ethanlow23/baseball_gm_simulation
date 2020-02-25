"""
0-4: .020
5-9: .040
10-14: .060
15-19: .080
20-24: .100
25-29: .115
30-34: .130
35-39: .145
40-44: .160
45-49: .175
50-54: .190
55-59: .200
60-64: .220
65-69: .240
70-74: .260
75-79: .280
80-84: .300
85-89: .320
90-94: .340
95-99: .360
"""

home_lineup = [
    {"position": "LF", "contact": 86},
    {"position": "CF", "contact": 79},
    {"position": "RF", "contact": 88},
    {"position": "3B", "contact": 89},
    {"position": "SS", "contact": 77},
    {"position": "2B", "contact": 71},
    {"position": "1B", "contact": 69},
    {"position": "C", "contact": 71},
    {"position": "DH", "contact": 75}
]
home_pitcher = {"position": "P", "rating": 89}
away_lineup = [
    {"position": "LF", "contact": 92},
    {"position": "CF", "contact": 83},
    {"position": "RF", "contact": 92},
    {"position": "3B", "contact": 89},
    {"position": "SS", "contact": 83},
    {"position": "2B", "contact": 77},
    {"position": "1B", "contact": 71},
    {"position": "C", "contact": 74},
    {"position": "DH", "contact": 77}
]
away_pitcher = {"position": "P", "rating": 78}

import random

away_score = 0
home_score = 0
half_inning = 0
away_outs = 0
home_outs = 0
first_base = False
second_base = False
third_base = False
away_plate_appearances = 0
home_plate_appearances = 0

home_box_score = [
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0}
]
away_box_score = [
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0},
    {"at_bats": 0, "hits": 0}
]

while (away_outs < 27 or home_outs < 24):
    if (half_inning == 0):
        while (away_outs % 3 == 0):
            batter = away_lineup[away_plate_appearances % 9]
            away_box_score[away_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - home_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                away_box_score[away_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    away_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                away_outs += 1
            away_plate_appearances += 1
        while (away_outs % 3 != 0):
            batter = away_lineup[away_plate_appearances % 9]
            away_box_score[away_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - home_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                away_box_score[away_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    away_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                away_outs += 1
            away_plate_appearances += 1
        first_base = False
        second_base = False
        third_base = False
        half_inning = 1
        print("End of top half of inning...")
    else:
        while (home_outs % 3 == 0):
            batter = home_lineup[home_plate_appearances % 9]
            home_box_score[home_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                home_box_score[home_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    home_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                home_outs += 1
            home_plate_appearances += 1
        while (home_outs % 3 != 0):
            batter = home_lineup[home_plate_appearances % 9]
            home_box_score[home_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                home_box_score[home_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    home_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                home_outs += 1
            home_plate_appearances += 1
        first_base = False
        second_base = False
        third_base = False
        half_inning = 0
        print("End of bottom half of inning...")
if (away_score >= home_score):
    while (home_outs % 3 == 0):
        batter = home_lineup[home_plate_appearances % 9]
        home_box_score[home_plate_appearances % 9]["at_bats"] += 1
        matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
        pitch = random.randint(0, 1000)
        if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
            print("HIT")
            home_box_score[home_plate_appearances % 9]["hits"] += 1
            if (third_base and second_base and first_base):
                home_score += 1
            elif (second_base and first_base):
                third_base = True
            elif (first_base):
                second_base = True
            else:
                first_base = True
        else:
            print("OUT")
            home_outs += 1
        home_plate_appearances += 1
    while (home_outs % 3 != 0):
        batter = home_lineup[home_plate_appearances % 9]
        home_box_score[home_plate_appearances % 9]["at_bats"] += 1
        matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
        pitch = random.randint(0, 1000)
        if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
            print("HIT")
            home_box_score[home_plate_appearances % 9]["hits"] += 1
            if (third_base and second_base and first_base):
                home_score += 1
            elif (second_base and first_base):
                third_base = True
            elif (first_base):
                second_base = True
            else:
                first_base = True
        else:
            print("OUT")
            home_outs += 1
        home_plate_appearances += 1
    first_base = False
    second_base = False
    third_base = False
    half_inning = 0
    print("End of bottom half of inning...")
print("End of 9th inning")
print("Score is away " + str(away_score) + "-" + str(home_score) + " home")
while (away_score == home_score):
    if (half_inning == 0):
        while (away_outs % 3 == 0):
            batter = away_lineup[away_plate_appearances % 9]
            away_box_score[away_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - home_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                away_box_score[away_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    away_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                away_outs += 1
            away_plate_appearances += 1
        while (away_outs % 3 != 0):
            batter = away_lineup[away_plate_appearances % 9]
            away_box_score[away_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - home_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                away_box_score[away_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    away_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                away_outs += 1
            away_plate_appearances += 1
        first_base = False
        second_base = False
        third_base = False
        half_inning = 1
        print("End of top half of inning...")
    if (half_inning == 1):
        while (home_outs % 3 == 0):
            batter = home_lineup[home_plate_appearances % 9]
            home_box_score[home_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                home_box_score[home_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    home_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                home_outs += 1
            home_plate_appearances += 1
        while (home_outs % 3 != 0):
            batter = home_lineup[home_plate_appearances % 9]
            home_box_score[home_plate_appearances % 9]["at_bats"] += 1
            matchup_multiplier = ((batter["contact"] - away_pitcher["rating"]) / 100) + 1
            pitch = random.randint(0, 1000)
            if ((batter["contact"] * 3.6) * matchup_multiplier >= pitch):
                print("HIT")
                home_box_score[home_plate_appearances % 9]["hits"] += 1
                if (third_base and second_base and first_base):
                    home_score += 1
                elif (second_base and first_base):
                    third_base = True
                elif (first_base):
                    second_base = True
                else:
                    first_base = True
            else:
                print("OUT")
                home_outs += 1
            home_plate_appearances += 1
        first_base = False
        second_base = False
        third_base = False
        half_inning = 0
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