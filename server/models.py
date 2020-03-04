class League(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    teams = db.relationship('Team', backref='league')
    players = db.relationship('Player', backref='league')

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), nullable=False)
    players = db.relationship('Player', backref='team')

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

class Team_Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    at_bats = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    doubles = db.Column(db.Integer)
    triples = db.Column(db.Integer)
    homeruns = db.Column(db.Integer)
    rbis = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

class Player_Stat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    at_bats = db.Column(db.Integer)
    hits = db.Column(db.Integer)
    doubles = db.Column(db.Integer)
    triples = db.Column(db.Integer)
    homeruns = db.Column(db.Integer)
    rbis = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
