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
  player_info = {'name': '{} {}'.format(player.first_name,player.last_name), 'team': player.team.city + ' ' + player.team.name, 'games': []}
  for log in player.player_stats:
    info = {}
    info['game_id'] = log.game.id
    info['away_team'] = log.game.away.serialize()
    info['home_team'] = log.game.home.serialize()
    info['stats'] = log.serialize()
    player_info['games'].append(info)
  return jsonify(player_info)

@player_api.route('/<player_id>/stats')
def player_stats(player_id):
  player = Player.query.get(player_id)
  career_stats = {}
  for log in player.player_stats:
    if log.season.year not in career_stats:
      career_stats[log.season.year] = {'AB': log.at_bats, 'H': log.hits, '2B': log.doubles, '3B': log.triples, 'HR': log.homeruns, 'RBI': log.rbi}
    else:
      career_stats[log.season.year]['AB'] += log.at_bats
      career_stats[log.season.year]['H'] += log.hits
      career_stats[log.season.year]['2B'] += log.doubles
      career_stats[log.season.year]['3B'] += log.triples
      career_stats[log.season.year]['HR'] += log.homeruns
      career_stats[log.season.year]['RBI'] += log.rbi
  return jsonify(career_stats)
