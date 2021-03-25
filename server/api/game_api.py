from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

game_api = Blueprint('game_api', __name__)

# GET ALL GAMES
@game_api.route('/')
def games():
    all_games = Game.query.filter(Game.team_stats.any())
    return jsonify([game.serialize() for game in all_games])

# GET ALL GAMES BY GAME NUMBER
@game_api.route('/number/<game_number>')
def games_number(game_number):
    all_games = Game.query.filter_by(game_number=game_number)
    results = []
    for game in all_games:
        box_scores = {}
        t1 = game.team_stats[0]
        t1_city = t1.team.city
        t1_score = t1.rbi
        t1_team_stats = t1.serialize()
        t1_player_stats = [player_stat.serialize() for player_stat in game.player_stats if player_stat.player.team == t1.team]
        t2 = game.team_stats[1]
        t2_city = t2.team.city
        t2_score = t2.rbi
        t2_team_stats = t2.serialize()
        t2_player_stats = [player_stat.serialize() for player_stat in game.player_stats if player_stat.player.team == t2.team]
        t1_box_score = {'score': t1_score, 'team stats': t1_team_stats, 'player stats': t1_player_stats}
        box_scores[t1_city] = t1_box_score
        t2_box_score = {'score': t2_score, 'team stats': t2_team_stats, 'player stats': t2_player_stats}
        box_scores[t2_city] = t2_box_score
        results.append(box_scores)
    return jsonify(results)
    '''
    return jsonify([game.serialize() for game in all_games])
    '''

# GET A GAME
@game_api.route('/<game_id>')
def game(game_id):
    game = Game.query.get(game_id)
    game_info = {'away': '{} {}'.format(game.away.city, game.away.name), 'home': '{} {}'.format(game.home.city, game.home.name), 'away_player_stats': [], 'home_player_stats': []}
    for team_stat in game.team_stats:
        if team_stat.team == game.away:
            game_info['away_score'] = team_stat.rbi
            game_info['away_team_stats'] = team_stat.serialize()
        else:
            game_info['home_score'] = team_stat.rbi
            game_info['home_team_stats'] = team_stat.serialize()
    for player_stat in game.player_stats:
        player_info = {'id': player_stat.player.id, 'name': '{} {}'.format(player_stat.player.first_name, player_stat.player.last_name), 'stats': player_stat.serialize()}
        if player_stat.player.team == game.away:
            game_info['away_player_stats'].append(player_info)
        else:
            game_info['home_player_stats'].append(player_info) 
    return jsonify(game_info)
    '''
    box_score = {}
    t1 = game.team_stats[0]
    t1_team = '{} {}'.format(t1.team.city, t1.team.name)
    t1_score = t1.rbi
    t1_team_stats = t1.serialize()
    t1_player_stats = [player_stat.serialize() for player_stat in game.player_stats if player_stat.player.team == t1.team]
    t2 = game.team_stats[1]
    t2_team = '{} {}'.format(t2.team.city, t2.team.name)
    t2_score = t2.rbi
    t2_team_stats = t2.serialize()
    t2_player_stats = [player_stat.serialize() for player_stat in game.player_stats if player_stat.player.team == t2.team]
    box_score['t1'] = t1_team
    box_score['t1_score'] = t1_score
    box_score['t1_team_stats'] = t1_team_stats
    box_score['t1_player_stats'] = t1_player_stats
    box_score['t2'] = t2_team
    box_score['t2_score'] = t2_score
    box_score['t2_team_stats'] = t2_team_stats
    box_score['t2_player_stats'] = t2_player_stats
    return jsonify(box_score)
    '''
