from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DB_USERNAME, DB_PASSWORD, DB_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@localhost/{}'.format(DB_USERNAME, DB_PASSWORD, DB_NAME)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    teams = db.relationship('Team', backref='league')
    players = db.relationship('Player', backref='league')

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "teams": [team.serialize() for team in self.teams],
            "players": [player.serialize() for player in self.players]
        }

game_teams = db.Table('game_teams',
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('team.id'), primary_key=True)
)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    players = db.relationship('Player', backref='team')
    team_stats = db.relationship('Team_Stat', backref='team')
    games = db.relationship('Game', secondary=game_teams, backref='teams')

    def serialize(self):
        return {
            "id": self.id,
            "city": self.city,
            "name": self.name,
            "league_id": self.league_id,
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
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    player_stats = db.relationship('Player_Stat', backref='player')

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
            "league_id": self.league_id,
            "team_id": self.team_id,
            "player_stats": [player_stat.serialize() for player_stat in self.player_stats]
        }

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    game_number = db.Column(db.Integer, nullable=False)
    home_score = db.Column(db.Integer, nullable=False, default=0)
    away_score = db.Column(db.Integer, nullable=False, default=0)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "game_number": self.game_number,
            "home_score": self.home_score,
            "away_score": self.away_score
        }

class Team_Stat(db.Model):
    __tablename__ = "team_stat"

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    wins = db.Column(db.Integer, nullable=False, default=0)
    losses = db.Column(db.Integer, nullable=False, default=0)
    at_bats = db.Column(db.Integer, nullable=False, default=0)
    hits = db.Column(db.Integer, nullable=False, default=0)
    doubles = db.Column(db.Integer, nullable=False, default=0)
    triples = db.Column(db.Integer, nullable=False, default=0)
    homeruns = db.Column(db.Integer, nullable=False, default=0)
    rbi = db.Column(db.Integer, nullable=False, default=0)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "wins": self.wins,
            "losses": self.losses,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "doubles": self.doubles,
            "triples": self.triples,
            "homeruns": self.homeruns,
            "rbi": self.rbi,
            "team_id": self.team_id
        }

class Player_Stat(db.Model):
    __tablename__ = "player_stat"

    id = db.Column(db.Integer, primary_key=True)
    season = db.Column(db.Integer, nullable=False)
    at_bats = db.Column(db.Integer, nullable=False, default=0)
    hits = db.Column(db.Integer, nullable=False, default=0)
    doubles = db.Column(db.Integer, nullable=False, default=0)
    triples = db.Column(db.Integer, nullable=False, default=0)
    homeruns = db.Column(db.Integer, nullable=False, default=0)
    rbi = db.Column(db.Integer, nullable=False, default=0)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "season": self.season,
            "at_bats": self.at_bats,
            "hits": self.hits,
            "doubles": self.doubles,
            "triples": self.triples,
            "homeruns": self.homeruns,
            "rbi": self.rbi,
            "player_id": self.player_id
        }

from api.home_api import home_api

app.register_blueprint(home_api)
