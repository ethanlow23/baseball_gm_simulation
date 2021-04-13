from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_USERNAME, DB_PASSWORD, DB_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@localhost/{}'.format(DB_USERNAME, DB_PASSWORD, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # league = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=True, nullable=False)
    teams = db.relationship('Team', backref='season')
    players = db.relationship('Player', backref='season')
    games = db.relationship('Game', backref='season')
    team_stats = db.relationship('Team_Stat', backref='season')
    player_stats = db.relationship('Player_Stat', backref='season')

    def serialize(self):
        return {
            "id": self.id,
            # "league": self.league,
            "year": self.year,
            "teams": [team.serialize() for team in self.teams],
            "players": [player.serialize() for player in self.players],
            "games": [game.serialize() for game in self.games]
        }

game_players = db.Table('game_players',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True)
)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    players = db.relationship('Player', backref='team')
    team_stats = db.relationship('Team_Stat', backref='team')
    player_stats = db.relationship('Player_Stat', backref='team')
    games = db.relationship('Game', primaryjoin='or_(Team.id==Game.home_id, Team.id==Game.away_id)')
    # home_games = db.relationship('Game', foreign_keys='Game.home_id', backref='home')
    # away_games = db.relationship('Game', foreign_keys='Game.away_id', backref='away')

    def serialize(self):
        return {
            "id": self.id,
            "city": self.city,
            "name": self.name,
            "season_id": self.season_id,
            "players": [player.serialize() for player in self.players],
            "team_stats": [team_stat.serialize() for team_stat in self.team_stats],
            "games": [game.serialize() for game in self.games]
        }

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    position = db.Column(db.String(80), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    power = db.Column(db.Integer, nullable=False)
    velocity = db.Column(db.Integer, nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    player_stats = db.relationship('Player_Stat', backref='player')
    games = db.relationship('Game', secondary=game_players, backref='players')

    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "position": self.position,
            "contact": self.contact,
            "power": self.power,
            "velocity": self.velocity,
            "season_id": self.season_id,
            "team_id": self.team_id,
            "player_stats": [player_stat.serialize() for player_stat in self.player_stats]
        }

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_number = db.Column(db.Integer, nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)
    home_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    away_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_score = db.Column(db.Integer, nullable=False, default=0)
    away_score = db.Column(db.Integer, nullable=False, default=0)
    # team_stats = db.relationship('Team_Stat', backref='game')
    home_team_stat = db.relationship('Team_Stat', uselist=False, primaryjoin='and_(Game.id==Team_Stat.game_id, Game.home_id==Team_Stat.team_id)')
    away_team_stat = db.relationship('Team_Stat', uselist=False, primaryjoin='and_(Game.id==Team_Stat.game_id, Game.away_id==Team_Stat.team_id)')
    # player_stats = db.relationship('Player_Stat', backref='game')
    home_player_stats = db.relationship('Player_Stat', primaryjoin='and_(Game.id==Player_Stat.game_id, Game.home_id==Player_Stat.team_id)')
    away_player_stats = db.relationship('Player_Stat', primaryjoin='and_(Game.id==Player_Stat.game_id, Game.away_id==Player_Stat.team_id)')

    home = db.relationship('Team', foreign_keys='Game.home_id')
    away = db.relationship('Team', foreign_keys='Game.away_id')
    
    def serialize(self):
        return {
            "id": self.id,
            "game_number": self.game_number,
            "season_id": self.season_id,
            "home_id": self.home_id,
            "away_id": self.away_id,
            "home_score": self.home_score,
            "away_score": self.away_score,
            "home_team_stat": self.home_team_stat.serialize() if self.home_team_stat else None,
            "away_team_stat": self.away_team_stat.serialize() if self.away_team_stat else None,
            "home_player_stats": [home_player_stat.serialize() for home_player_stat in self.home_player_stats],
            "away_player_stats": [away_player_stat.serialize() for away_player_stat in self.away_player_stats],
        }

class Team_Stat(db.Model):
    __tablename__ = "team_stat"

    id = db.Column(db.Integer, primary_key=True)
    at_bats = db.Column(db.Integer, nullable=False, default=0)
    hits = db.Column(db.Integer, nullable=False, default=0)
    doubles = db.Column(db.Integer, nullable=False, default=0)
    triples = db.Column(db.Integer, nullable=False, default=0)
    homeruns = db.Column(db.Integer, nullable=False, default=0)
    rbi = db.Column(db.Integer, nullable=False, default=0)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)

    game = db.relationship('Game', foreign_keys='Team_Stat.game_id')

    def serialize(self):
        return {
            "id": self.id,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "doubles": self.doubles,
            "triples": self.triples,
            "homeruns": self.homeruns,
            "rbi": self.rbi,
            "team_id": self.team_id,
            "game_id": self.game_id,
            "season_id": self.season_id
        }

class Player_Stat(db.Model):
    __tablename__ = "player_stat"

    id = db.Column(db.Integer, primary_key=True)
    at_bats = db.Column(db.Integer, nullable=False, default=0)
    hits = db.Column(db.Integer, nullable=False, default=0)
    doubles = db.Column(db.Integer, nullable=False, default=0)
    triples = db.Column(db.Integer, nullable=False, default=0)
    homeruns = db.Column(db.Integer, nullable=False, default=0)
    rbi = db.Column(db.Integer, nullable=False, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    season_id = db.Column(db.Integer, db.ForeignKey('season.id'), nullable=False)

    game = db.relationship('Game', foreign_keys='Player_Stat.game_id')

    def serialize(self):
        return {
            "id": self.id,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "doubles": self.doubles,
            "triples": self.triples,
            "homeruns": self.homeruns,
            "rbi": self.rbi,
            "player_id": self.player_id,
            "team_id": self.team_id,
            "game_id": self.game_id,
            "season_id": self.season_id
        }

from api.home_api import home_api
from api.league_api import league_api
from api.team_api import team_api
from api.player_api import player_api
from api.game_api import game_api

app.register_blueprint(home_api)
app.register_blueprint(league_api, url_prefix='/league')
app.register_blueprint(team_api, url_prefix='/teams')
app.register_blueprint(player_api, url_prefix='/players')
app.register_blueprint(game_api, url_prefix='/games')
