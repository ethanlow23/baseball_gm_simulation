from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

team_api = Blueprint('team_api', __name__)

# GET A TEAM
@team_api.route('/<team_id>')
def team(team_id):
    team = Team.query.get(team_id)
    return jsonify(team.serialize())

# GET A TEAM'S OVERVIEW
@team_api.route('/<team_id>/overview')
def team_overview(team_id):
  team_overview = {}
  team_overview['wins'] = 0
  team_overview['losses'] = 0
  recent_results = Game.query.filter((Game.home_id==team_id) | (Game.away_id==team_id)).filter(Game.home_team_stat.has()).order_by(Game.game_number.desc()).limit(5)
  team_overview['recent_results'] = [recent_result.serialize() for recent_result in recent_results]
  upcoming_games = Game.query.filter((Game.home_id==team_id) | (Game.away_id==team_id)).filter(~Game.home_team_stat.has()).limit(5)
  team_overview['upcoming_games'] = [upcoming_game.serialize() for upcoming_game in upcoming_games]
  team_overview['top_performers'] = []
  return jsonify(team_overview)

# GET A TEAM'S SCHEDULE
@team_api.route('/<team_id>/schedule')
def team_games(team_id):
  team_games = Game.query.filter((Game.home_id==team_id) | (Game.away_id==team_id)).order_by('game_number')
  games = []
  for game in team_games:
    game_info = {'id': game.id, 'game_number': game.game_number, 'home_team': '{} {}'.format(game.home.city, game.home.name), 'away_team': '{} {}'.format(game.away.city, game.away.name)}
    games.append(game_info)
  return jsonify(games)

# GET A TEAM'S ROSTER
@team_api.route('/<team_id>/roster')
def team_roster(team_id):
  roster = Team.query.get(team_id).players
  return jsonify([player.serialize() for player in roster])

# GET A TEAM'S STATS
@team_api.route('/<team_id>/stats')
def team_stats(team_id):
  players = Team.query.get(team_id).players
  stats = {'batters': [], 'pitchers': []}
  for player in players:
    if player.position != 'SP':
      batter_stats = {'player': player.serialize()}
      for log in player.player_stats:
        batter_stats['AB'] = batter_stats.get('AB', 0) + log.at_bats
        batter_stats['H'] = batter_stats.get('H', 0) + log.hits
        batter_stats['2B'] = batter_stats.get('2B', 0) + log.doubles
        batter_stats['3B'] = batter_stats.get('3B', 0) + log.triples
        batter_stats['HR'] = batter_stats.get('HR', 0) + log.homeruns
        batter_stats['RBI'] = batter_stats.get('RBI', 0) + log.rbi
      stats['batters'].append(batter_stats)
    else:
      pitcher_stats = {'player': player.serialize()}
      stats['pitchers'].append(pitcher_stats)
  return jsonify(stats)
