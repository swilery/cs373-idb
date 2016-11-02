import os
import unittest
from loader import db, app_instance
from models import Source, Article, Location
# from sqlalchemy.orm import sessionmaker
# from datetime import datetime
# from dateutil import parser
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
    def test_source_insert_1(self):
        source_repr = {"name": "BBC News", "cntry": "GB", "logo": "https:\\\\alogo.com",
            "lang": "EN", "desc": "British news at its finest, cheerio chap"}
        s = Source(**source_repr)
        self.session.add(s)

        r = self.session.query(Source).filter(Source.name == "BBC News").first()
        self.assertEqual(r.name, "BBC News")
        self.assertEqual(r.country, "GB")
        self.assertEqual(r.logo, "https:\\\\alogo.com")
        self.assertEqual(r.lang, "EN")
        self.assertEqual(r.desc, "British news at its finest, cheerio chap")

    def test_source_insert_2(self):
        source_repr = {"name": "Best News Ever", "cntry": "ST", "logo": "circles and stuff",
            "lang": "GR", "desc": "What even goes here, I don't know man"}
        s = Source(**source_repr)
        self.session.add(s)

        r = self.session.query(Source).filter(Source.name== "Best News Ever").first()
        self.assertEqual(r.name, "Best News Ever")
        self.assertEqual(r.country, "ST")
        self.assertEqual(r.logo, "circles and stuff")
        self.assertEqual(r.lang, "EN")
        self.assertEqual(r.desc, "What even goes here, I don't know man")
    
    def test_source_insert_3(self):
        source_repr = {"name": "Onion News Network", "cntry": "US", "logo": "A GIANT ONION",
            "lang": "EN", "desc": "Guaranteed accuracy and truthiness"}
        s = Source(**source_repr)
        self.session.add(s)

        r = self.session.query(Source).filter(Source.name == "").first()
        self.assertEqual(r.name, "Onion News Network")
        self.assertEqual(r.country, "EN")
        self.assertEqual(r.logo, "A GIANT ONION")
        self.assertEqual(r.lang, "EN")
        self.assertEqual(r.desc, "Guaranteed accuracy and truthiness")   

    # Insert articles
    def test_location_insert_1(self):
        location_repr = {"name": "Stevelandia", "region": "Upper western", "currency": "doubloon",
                        "lat_long": "42/42", "captial": "St. Elmo", "pop": "42000000"}
        l = Location(**location_repr)
        self.session.add(l)

        r = self.session.query(Location).filter(Location.name == "Stevelandia").first()
        self.assertEqual(r.name, "Stevelandia")
        self.assertEqual(r.region, "Upper western")
        self.assertEqual(r.currency, "doubloon")
        self.assertEqual(r.lat_long, "42/42")
        self.assertEqual(r.capital, "St. Elmo")
        self.assertEqual(r.pop, "42000000")

    def test_location_insert_2(self):
        location_repr = {"name": "United Kingdom", "region": "Europe", "currency": "GBP",
                        "lat_long": "54,-2", "captial": "London", "pop": "64800000"}
        l = Location(**location_repr)
        self.session.add(l)

        r = self.session.query(Location).filter(Location.name == "United Kingdom").first()
        self.assertEqual(r.name, "United Kingdom")
        self.assertEqual(r.region, "Europe")
        self.assertEqual(r.currency, "GBP")
        self.assertEqual(r.lat_long, "54,-2")
        self.assertEqual(r.capital, "London")
        self.assertEqual(r.pop, "64800000")

    def test_location_insert_3(self):
        location_repr = {"name": "Italy", "region": "Europe", "currency": "EUR",
                        "lat_long": "42.83,12.83", "captial": "Rome", "pop": "60753794"}
        l = Location(**location_repr)
        self.session.add(l)

        r = self.session.query(Location).filter(Location.name == "Italy").first()
        self.assertEqual(r.name, "Italy")
        self.assertEqual(r.region, "Europe")
        self.assertEqual(r.currency, "EUR")
        self.assertEqual(r.lat_long, "42.83,12.83")
        self.assertEqual(r.capital, "Rome")
        self.assertEqual(r.pop, "60753794")

    # Insert articles
    def test_article_insert_1(self):
        location_repr = {"title": "Steve makes epic jump on bike", "excerpt": "Yo dog", "source": "BBC News",
                        "location": "", "pubDate": "2016-10-17T12:35:12Z", "author": "BBC News"}
        a = Article(**article_repr)
        self.session.add(a)

        r = self.session.query(Article).filter(Article.title == "Steve makes epic jump on bike").first()
        self.assertEqual(r.excerpt, "Yo dog")
        self.assertEqual(r.source, "BBC News")
        self.assertEqual(r.location, "")
        self.assertEqual(r.pubDate, "2016-10-17T12:35:12Z")
        self.assertEqual(r.author, "BBC News")

    def test_article_insert_2(self):
        location_repr = {"title": "In deep-red Florida, signs of trouble for Donald Trump", 
            "excerpt": "Some residents of The Villages, a GOP stronghold in Florida, are so disgusted with Donald Trump that they're backing Hillary Clinton for president.",
            "source": "USA Today",
            "location": "", 
            "pubDate": "2016-10-17T12:20:39Z", 
            "author": "Ledyard King"}
        a = Article(**article_repr)
        self.session.add(a)

        r = self.session.query(Article).filter(Article.title == "Steve makes epic jump on bike").first()
        self.assertEqual(r.title, "In deep-red Florida, signs of trouble for Donald Trump")
        self.assertEqual(r.excerpt, "Some residents of The Villages, a GOP stronghold in Florida, are so disgusted with Donald Trump that they're backing Hillary Clinton for president.")
        self.assertEqual(r.source, "USA Today")
        self.assertEqual(r.location, "")
        self.assertEqual(r.pubDate, "2016-10-17T12:20:39Z")
        self.assertEqual(r.author, "Ledyard King")

    def test_article_insert_3(self):
        location_repr = {"title": "Official: Icardi remains Inter captain", 
            "excerpt": "Mauro Icardi “will be sanctioned” by Inter, but the striker will not be stripped of the captaincy.", 
            "source": "Football Italia",
            "location": "", 
            "pubDate": "2016-10-17T01:00:00Z", 
            "author": "Football Italia Staff"}
        a = Article(**article_repr)
        self.session.add(a)

        r = self.session.query(Article).filter(Article.title == "Official: Icardi remains Inter captain").first()
        self.assertEqual(r.excerpt, "Mauro Icardi “will be sanctioned” by Inter, but the striker will not be stripped of the captaincy.")
        self.assertEqual(r.source, "Football Italia")
        self.assertEqual(r.location, "")
        self.assertEqual(r.pubDate, "2016-10-17T01:00:00Z")
        self.assertEqual(r.author, "Football Italia Staff")

if __name__ == '__main__':
    app_instance.config["TESTING"] = True
    app_instance.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('BESTBYTES_DB_TEST')
    # db.create_all()
    unittest.main()
    # db.drop_all()