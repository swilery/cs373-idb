# from loader import db
# from sqlalchemy_searchable import SearchQueryMixin
# from sqlalchemy_utils.types import TSVectorType
# from sqlalchemy_searchable import make_searchable
# from flask.ext.sqlalchemy import BaseQuery

# make_searchable()

# # !!!! Our current UML model has no many to many relationships !!!!

# # source_article = db.Table('source_article',
# #     db.Column('source_id', db.Integer, db.ForeignKey('sources_id')),
# #     db.Column('article_id')
# # )

# # source_location = db.Table('source_location',

# # )

# # article_location = db.Table('article_location', 

# # )


# class ArticleQuery(BaseQuery, SearchQueryMixin):
#     pass

# class SourceQuery(BaseQuery, SearchQueryMixin):
#     pass

# class LocationQuery(BaseQuery, SearchQueryMixin):
#     pass

# # articles - source (many to one)
# class Article(db.Model):
#     __tablename__ = 'articles'
#     '''
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     short = db.Column(db.String(10))
#     '''
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.Text)
#     excerpt = db.Column(db.String(50))
#     source_id = db.Column(db.Integer, ForeignKey('sources.id'))
#     source = relationship("Source", back_populates="articles")
#     # not all articles are given a location -> nullable true
#     location_id = db.Column(db.Integer, ForeignKey('locations.id'), nullable=True)
#     pubDate = db.Column(db.String(25))
#     author = db.Column(db.String(50))

#     search_vector = db.Column(TSVectorType('name'))

#     def to_json(self, list_view=False):
#         json_article = {
#             'id': self.id,
#             'name': self.title,
#             'excerpt': self.excerpt,
#             'source': self.source,
#             'publishedAt': self.pubDate,
#             'author': self.author,
#         }

#         return json_location

#     def __repr__(self):
#         return '<Article %s>' % self.short

# # template enum for languages
# import enum
# class langEnum(enum.Enum):
#     en = "English"

# # source - articles (one to many)
# class Source(db.Model):
#     __tablename__ = 'sources'
#     id = db.Column(db.Integer, primary_key=True)
#     logo = db.Column(db.String(255)) # URL
#     name = db.Column(db.String(50))
#     cnty = db.Column(db.String(50))
#     lang = db.Column(db.String(25))
#     desc = db.Column(db.Text)
#     articles = relationship("Article", back_populates="sources")
#     location_id = db.Column(db.Integer, ForeignKey('location.id'))
#     location = relationship("Location", back_populates="sources")

#     search_vector = db.Column(TSVectorType('name'))

#     def to_json(self, list_view=False):
#         json_location = {
#             'id': self.id,
#             'name': self.name,
#             'logo': self.logo,
#             'country': self.cnty,
#             'lang': self.lang,
#             'description': self.desc
#         }
#         if list_view:
#             art_list = []
#             for art in self.articles:
#                 details = {'id': src.id, 'name': src.name}
#                 art_list.append(details)

#         json_location['sources'] = src_list

#         return json_location

#     def __repr__(self):
#         return '<Source %r>' % self.name

# # source - location (one to many) -> sources all have a location/region, locations may have many sources
# # article - location (zero/one to many) -> some articles do not have a location
# class Location(db.Model):
#     __tablename__ = 'locations'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     region = db.Column(db.String(50))
#     currency = db.Column(db.String(10))
#     lat_long = db.Column(db.String(25))
#     capital = db.Column(db.String(50))
#     pop = db.Column(db.BigINT)
#     sources = relationship("Source", back_populates="locations")

#     search_vector = db.Column(TSVectorType('name'))

#     def to_json(self, list_view=False):
#         json_location = {
#             'id': self.id,
#             'name': self.name,
#             'region': self.region,
#             'currency': self.currency,
#             'lat_long': self.lat_long,
#             'capital': self.capital,
#             'pop': self.pop
#         }
#         if list_view:
#             src_list = []
#             for src in self.sources:
#                 details = {'id': src.id, 'name': src.name}
#                 src_list.append(details)
#         json_location['sources'] = src_list

#         return json_person

#     def __repr__(self):
#         return '<Location %s>' % self.name
