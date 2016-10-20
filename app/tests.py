import os
import unittest
from loader import db, app_instance
from models import Company, Person, Game, Platform
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from dateutil import parser
from flask import Flask

class DBTestCases(unittest.TestCase):
    def setUp(self):
        self.connection = db.engine.connect()
        self.trans = self.connection.begin()
        Session = sessionmaker(bind=db.engine)
        self.session = Session()

    def tearDown(self):
        self.session.rollback()

    # Insert sources
    def test_source_insert(self):
        source_repr = {"name": "BBC News", "cntry": "GB"}
        s = Source(**source_repr)
        self.session.add(s)

        r = self.session.query(Source).filter(Source.city == "").first()
        self.assertEqual(r.name, "BBC News")
        self.assertEqual(r.country, "GB")
       

    # Insert articles
    def test_location_insert(self):
        location_repr = {"name": "Stevelandia", "region": "Upper western", "currency": "doubloon",
                        "lat_long": "42/42", "captial": "St. Elmo", "pop": "42"}
        l = Location(**location_repr)
        self.session.add(l)

        r = self.session.query(Location).filter(Location.title == "Steve makes epic jump on bike").first()
        self.assertEqual(r.name, "Stevelandia")
        self.assertEqual(r.region, "Upper western")
        self.assertEqual(r.currency, "doubloon")

    # Insert articles
    def test_article_insert(self):
        location_repr = {"title": "Steve makes epic jump on bike", "excerpt": "Yo dog", "source": "BBC News",
                        "location": "", "pubDate": "2016-10-17T12:35:12Z", "author": "BBC News"}
        a = Article(**article_repr)
        self.session.add(a)

        r = self.session.query(Article).filter(Article.title == "Steve makes epic jump on bike").first()
        self.assertEqual(r.excerpt, "Yo dog")
        self.assertEqual(r.source, "BBC News")
        self.assertEqual(r.location, "")
   

if __name__ == '__main__':
    app_instance.config["TESTING"] = True
    app_instance.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('BESTBYTES_DB_TEST')
    db.create_all()
    unittest.main()
    db.drop_all()