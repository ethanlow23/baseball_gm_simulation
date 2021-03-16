from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

player_api = Blueprint('player_api', __name__)

#GET A PLAYER
@player_api.route('/<player_id>')
def player(player_id):
  player = Player.query.get(player_id)
  return jsonify(player.serialize())

# GET A PLAYER'S GAME LOG
@player_api.route('/<player_id>/log')
def player_log(player_id):
  player = Player.query.get(player_id)
  player_info = {'name': player.first_name + ' ' + player.last_name, 'team': player.team.city + ' ' + player.team.name, 'games': []}
  for log in player.player_stats:
    info = {}
    info['game_teams'] = [team.serialize() for team in log.game.teams]
    info['stats'] = log.serialize()
    player_info['games'].append(info)
  return jsonify(player_info)
