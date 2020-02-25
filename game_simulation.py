home_lineup = [
    {"position": "LF", "rating": 280},
    {"position": "CF", "rating": 260},
    {"position": "RF", "rating": 330},
    {"position": "3B", "rating": 300},
    {"position": "SS", "rating": 310},
    {"position": "2B", "rating": 250},
    {"position": "1B", "rating": 230},
    {"position": "C", "rating": 250},
    {"position": "DH", "rating": 260}
]

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

while (home_outs < 27 or away_outs < 27):
    if (half_inning == 0):
        away_outs += 3
        away_plate_appearances += 3
        half_inning = 1
        print("End of top half of inning...")
    else:
        while (home_outs % 3 == 0):
            batter = home_lineup[home_plate_appearances % 9]
            pitch = random.randint(0, 1000)
            if (batter["rating"] >= pitch):
                print("HIT")
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
            pitch = random.randint(0, 1000)
            if (batter["rating"] >= pitch):
                print("HIT")
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
print("Final score is " + str(away_score) + "-" + str(home_score))