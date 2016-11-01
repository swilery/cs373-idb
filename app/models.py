from loader import db
from sqlalchemy_searchable import SearchQueryMixin
from sqlalchemy_utils.types import TSVectorType
from sqlalchemy_searchable import make_searchable
from flask_sqlalchemy import BaseQuery

make_searchable()

class ArticleQuery(BaseQuery, SearchQueryMixin):
    pass

class SourceQuery(BaseQuery, SearchQueryMixin):
    pass

class LocationQuery(BaseQuery, SearchQueryMixin):
    pass

"""
__tablename__ = 'articles'
id_num = unique string identifier, db.String(25)
title = string, db.Text
description = string, db.Text
pubDate = string, db.String(25)
image_link = string, db.Text
category = string, db.String(25)
external_article_link = string, db.Text
external_source_link = string, db.Text
source_name = string, db.String(25)
region = string, db.String(25)
"""
class Article(db.Model):
    __tablename__ = 'articles'
    id_num = db.Column(db.String(25), primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    pubDate = db.Column(db.String(25))
    image_link = db.Column(db.Text)
    category = db.Column(db.String(25))
    external_article_link = db.Column(db.Text)
    external_source_link = db.Column(db.Text)
    source_name = db.Column(db.String(25))
    region = db.Column(db.String(25))

    search_vector = db.Column(TSVectorType('title'))

    def to_json(self, list_view=False):
        json_article = {
            'id_num': self.id_num,
            'title': self.title,
            'description': self.description,
            'pubDate': self.pubDate,
            'image_link': self.image_link,
            'category': self.category,
            'external_article_link': self.external_article_link,
            'external_source_link': self.external_source_link,
            'source_name': self.source_name,
            'region': self.region
        }

        return json_article

    def __repr__(self):
        return '<Article %s>' % self.id_num

"""
__tablename__ = 'sources'
id_num = unique string identifier, db.String(25)
id_name = string, db.Text
language = string, db.String(25)
description = string, db.Text
smallLogoURL = string, db.Text
mediumLogoURL = string, db.Text
largeLogoURL = string, db.Text
category = string, db.String(25)
external_link = string, db.Text
name = string, db.String(25)
region = string, db.String(25)
country = string, db.String(25)
"""
class Source(db.Model):
    __tablename__ = 'sources'
    id_num = db.Column(db.String(25), primary_key=True)
    id_name = db.Column(db.Text)
    language = db.Column(db.String(25))
    description = db.Column(db.Text)
    smallLogoURL = db.Column(db.Text)
    mediumLogoURL = db.Column(db.Text)
    largeLogoURL = db.Column(db.Text)
    category = db.Column(db.String(25))
    external_link = db.Column(db.Text)
    name = db.Column(db.String(25))
    region = db.Column(db.String(25))
    country = db.Column(db.String(25))

    search_vector = db.Column(TSVectorType('name'))

    def to_json(self, list_view=False):
        json_location = {
            'id_num': self.id_num,
            'id_name': self.id_name,
            'language': self.language,
            'description': self.description,
            'smallLogoURL': self.smallLogoURL,
            'mediumLogoURL': self.mediumLogoURL,
            'largeLogoURL': self.largeLogoURL,
            'category': self.category,
            'external_link': self.external_link,
            'name': self.name,
            'region': self.region,
            'country': self.country
        }

        return json_location

    def __repr__(self):
        return '<Source %r>' % self.id_num

"""
__tablename__ = 'locations'
id_num = string, db.String(25)
currencies = string, db.Text
latlng = string, db.String(25)
capital = string, db.String(25)
population = string, db.String(25)
topLevelDomain = string, db.String(25)
languages = string, db.Text
name = string, db.String(25)
region = string, db.String(25)
"""
class Location(db.Model):
    __tablename__ = 'locations'
    id_num = db.Column(db.String(25), primary_key=True)
    currencies = db.Column(db.Text)
    latlng = db.Column(db.Text)
    capital = db.Column(db.String(50))
    population = db.Column(db.String(50))
    topLevelDomain = db.Column(db.Text)
    languages = db.Column(db.Text)
    name = db.Column(db.String(50))
    region = db.Column(db.String(25))

    search_vector = db.Column(TSVectorType('name'))

    def to_json(self, list_view=False):
        json_location = {
            'id_num': self.id_num,
            'currencies': self.currencies,
            'latlng': self.latlng,
            'capital': self.capital,
            'population': self.population,
            'topLevelDomain': self.topLevelDomain,
            'languages': self.languages,
            'name': self.name,
            'region': self.region
        }

        return json_location

    def __repr__(self):
        return '<Location %s>' % self.id_num
