from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

league_api = Blueprint('league_api', __name__)

# GET LEAGUE OVERVIEW
@league_api.route('/overview')
def overview():
  overview = {}
  top_teams = Team.query.limit(5)
  overview['top_teams'] = [team.serialize() for team in top_teams]
  top_players = Player.query.limit(5)
  overview['top_players'] = [player.serialize() for player in top_players]
  recent_results = Game.query.filter(Game.home_team_stat.has()).order_by(Game.game_number.desc()).limit(7)
  overview['recent_results'] = [game_result.serialize() for game_result in recent_results]
  upcoming_games = Game.query.filter(~Game.home_team_stat.has()).limit(7)
  overview['upcoming_games'] = [upcoming_game.serialize() for upcoming_game in upcoming_games]
  return jsonify(overview)

# GET ALL TEAMS
@league_api.route('/teams')
def teams():
  all_teams = Team.query.all()
  return jsonify([team.serialize() for team in all_teams])

# GET ALL TEAM STATS
@league_api.route('/stats')
def stats():
  teams = Team.query.all()
  teams_stats = []
  for team in teams:
    stats = {'team': team.serialize()}
    for stat in team.team_stats:
      stats['AB'] = stats.get('AB', 0) + stat.at_bats
      stats['H'] = stats.get('H', 0) + stat.hits
      stats['2B'] = stats.get('2B', 0) + stat.doubles
      stats['3B'] = stats.get('3B', 0) + stat.triples
      stats['HR'] = stats.get('HR', 0) + stat.homeruns
      stats['RBI'] = stats.get('RBI', 0) + stat.rbi
    teams_stats.append(stats)
  return jsonify(teams_stats)

@league_api.route('/leaders')
def leaders():
  return {'hello': 'world'}
