from app import db
from datetime import datetime

class Urls(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key=True)
    url_long = db.Column(db.String(500), nullable=False)
    url_short = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    clicks = db.Column(db.Integer, default=0)

    def __init__(self, url_long, url_short):
        self.url_long = url_long
        self.url_short = url_short

    def __repr__(self):
        return f'Short url: {self.url_short}. ' \
               f'Target: {self.url_long}. ' \
               f'Created on: {self.created_at.strftime("%m.%d.%Y at %H:%M:%S")}'