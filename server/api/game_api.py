from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

game_api = Blueprint('game_api', __name__)

# GET ALL GAMES
@game_api.route('/')
def games():
    all_games = Game.query.filter(Game.home_team_stat.has())
    return jsonify([game.serialize() for game in all_games])

# GET ALL GAMES BY GAME NUMBER
@game_api.route('/number/<game_number>')
def games_number(game_number):
    all_games = Game.query.filter_by(game_number=game_number)
    return jsonify([game.serialize() for game in all_games])

# GET A GAME
@game_api.route('/<game_id>')
def game(game_id):
    game = Game.query.get(game_id)
    game_info = game.serialize()
    game_info['away'] = game.away.serialize()
    game_info['home'] = game.home.serialize()
    for i in range(len(game.away_player_stats)):
        game_info['away_player_stats'][i]['player'] = game.away_player_stats[i].player.serialize()
    for i in range(len(game.home_player_stats)):
        game_info['home_player_stats'][i]['player'] = game.home_player_stats[i].player.serialize()
    return jsonify(game_info)
