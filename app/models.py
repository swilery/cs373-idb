from loader import db
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable
from flask.ext.sqlalchemy import BaseQuery

make_searchable()

# Association tables for many-to-many relationships
'''
company_person = db.Table('company_person',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
    db.Column('person_id', db.Integer, db.ForeignKey('people.id'))
)
developer_game = db.Table('developer_game',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'))
)
publisher_game = db.Table('publisher_game',
    db.Column('company_id', db.Integer, db.ForeignKey('companies.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'))
)
person_game = db.Table('person_game',
    db.Column('person_id', db.Integer, db.ForeignKey('people.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('games.id'))
)
game_platform = db.Table('game_platform',
    db.Column('game_id', db.Integer, db.ForeignKey('games.id')),
    db.Column('platform_id', db.Integer, db.ForeignKey('platforms.id'))
)
'''

class ArticleQuery(BaseQuery, SearchQueryMixin):
    pass

class SourceQuery(BaseQuery, SearchQueryMixin):
    pass

class LocationQuery(BaseQuery, SearchQueryMixin):
    pass


class Article(db.Model):
    __tablename__ = 'articles'
    '''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    short = db.Column(db.String(10))
    '''
    def __repr__(self):
        return '<Article %s>' % self.short


class Source(db.Model):
    __tablename__ = 'sources'
    
    def __repr__(self):
        return '<Source %r>' % self.name


class Location(db.Model):
    __tablename__ = 'locations'
    
    def __repr__(self):
        return '<Location %s>' % self.name
