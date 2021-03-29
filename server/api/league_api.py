from flask import Blueprint, request, jsonify
from app import db, Season, Team, Player, Game, Team_Stat, Player_Stat

league_api = Blueprint('league_api', __name__)

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
