import os
import unittest
from loader import db, app_instance
from models import Article, Source, Location

class DBTestCases(unittest.TestCase):

    # Insert sources
    def test_source_insert_1(self):
        s = Source(id_num='100', id_name='test-src1', language='elvish', \
            description='official news source of middle-earth', smallLogoURL='small.png', mediumLogoURL='medium.png', \
            largeLogoURL='large.png', category='general', external_link='some-link.com',name='Middle-Earth News',\
            region='fantasy', country='Mordor')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Source).filter(Source.name == 'Middle-Earth News').first()
        self.assertEqual(r.id_num, '100')
        self.assertEqual(r.id_name, 'test-src1')
        self.assertEqual(r.language, 'elvish')
        self.assertEqual(r.description, 'official news source of middle-earth')
        self.assertEqual(r.smallLogoURL, 'small.png')
        self.assertEqual(r.mediumLogoURL, 'medium.png')
        self.assertEqual(r.largeLogoURL, 'large.png')
        self.assertEqual(r.category, 'general')
        self.assertEqual(r.external_link, 'some-link.com')
        self.assertEqual(r.name, 'Middle-Earth News')
        self.assertEqual(r.region, 'fantasy')
        self.assertEqual(r.country, 'Mordor')

        db.session.query(Source).filter(Source.name == 'Middle-Earth News').delete()
        db.session.commit()

    def test_source_insert_2(self):
        s = Source(id_num='101', id_name='test-src2', language='latin', \
            description='official news source of the roman empire', smallLogoURL='small_logo.jpg', mediumLogoURL='medium_logo.jpg', \
            largeLogoURL='large_logo.jpg', category='history', external_link='barbarians-are-invading.com',name='Roma News',\
            region='Mediterranean Sea', country='Italia')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Source).filter(Source.external_link == 'barbarians-are-invading.com').first()
        self.assertEqual(r.id_num, '101')
        self.assertEqual(r.id_name, 'test-src2')
        self.assertEqual(r.language, 'latin')
        self.assertEqual(r.description, 'official news source of the roman empire')
        self.assertEqual(r.smallLogoURL, 'small_logo.jpg')
        self.assertEqual(r.mediumLogoURL, 'medium_logo.jpg')
        self.assertEqual(r.largeLogoURL, 'large_logo.jpg')
        self.assertEqual(r.category, 'history')
        self.assertEqual(r.external_link, 'barbarians-are-invading.com')
        self.assertEqual(r.name, 'Roma News')
        self.assertEqual(r.region, 'Mediterranean Sea')
        self.assertEqual(r.country, 'Italia')

        db.session.query(Source).filter(Source.external_link == 'barbarians-are-invading.com').delete()
        db.session.commit()
    
    def test_source_insert_3(self):
        s = Source(id_num='102', id_name='test-src3', language='English', \
            description='Guaranteed best source for accuracy and truthiness', smallLogoURL='http://assets3.onionstatic.com/onionstatic/onion/static/images/onion_fb_placeholder.png', mediumLogoURL='the_onion.gif', \
            largeLogoURL='the_onion2.img', category='The Truth', external_link='http://www.theonion.com/',name='The Onion',\
            region='United States', country='United States')
        db.session.add(s)
        db.session.commit()


        r = db.session.query(Source).filter(Source.id_num == '102').first()
        self.assertEqual(r.id_num, '102')
        self.assertEqual(r.id_name, 'test-src3')
        self.assertEqual(r.language, 'English')
        self.assertEqual(r.description, 'Guaranteed best source for accuracy and truthiness')
        self.assertEqual(r.smallLogoURL, 'http://assets3.onionstatic.com/onionstatic/onion/static/images/onion_fb_placeholder.png')
        self.assertEqual(r.mediumLogoURL, 'the_onion.gif')
        self.assertEqual(r.largeLogoURL, 'the_onion2.img')
        self.assertEqual(r.category, 'The Truth')
        self.assertEqual(r.external_link, 'http://www.theonion.com/')
        self.assertEqual(r.name, 'The Onion')
        self.assertEqual(r.region, 'United States')
        self.assertEqual(r.country, 'United States')

        db.session.query(Source).filter(Source.id_num == '102').delete()
        db.session.commit() 

    # # Insert articles
    # def test_location_insert_1(self):
    #     location_repr = {"name": "Stevelandia", "region": "Upper western", "currency": "doubloon",
    #                     "lat_long": "42/42", "captial": "St. Elmo", "pop": "42000000"}
    #     l = Location(**location_repr)
    #     self.session.add(l)

    #     r = self.session.query(Location).filter(Location.name == "Stevelandia").first()
    #     self.assertEqual(r.name, "Stevelandia")
    #     self.assertEqual(r.region, "Upper western")
    #     self.assertEqual(r.currency, "doubloon")
    #     self.assertEqual(r.lat_long, "42/42")
    #     self.assertEqual(r.capital, "St. Elmo")
    #     self.assertEqual(r.pop, "42000000")

    # def test_location_insert_2(self):
    #     location_repr = {"name": "United Kingdom", "region": "Europe", "currency": "GBP",
    #                     "lat_long": "54,-2", "captial": "London", "pop": "64800000"}
    #     l = Location(**location_repr)
    #     self.session.add(l)

    #     r = self.session.query(Location).filter(Location.name == "United Kingdom").first()
    #     self.assertEqual(r.name, "United Kingdom")
    #     self.assertEqual(r.region, "Europe")
    #     self.assertEqual(r.currency, "GBP")
    #     self.assertEqual(r.lat_long, "54,-2")
    #     self.assertEqual(r.capital, "London")
    #     self.assertEqual(r.pop, "64800000")

    # def test_location_insert_3(self):
    #     location_repr = {"name": "Italy", "region": "Europe", "currency": "EUR",
    #                     "lat_long": "42.83,12.83", "captial": "Rome", "pop": "60753794"}
    #     l = Location(**location_repr)
    #     self.session.add(l)

    #     r = self.session.query(Location).filter(Location.name == "Italy").first()
    #     self.assertEqual(r.name, "Italy")
    #     self.assertEqual(r.region, "Europe")
    #     self.assertEqual(r.currency, "EUR")
    #     self.assertEqual(r.lat_long, "42.83,12.83")
    #     self.assertEqual(r.capital, "Rome")
    #     self.assertEqual(r.pop, "60753794")

    # # Insert articles
    # def test_article_insert_1(self):
    #     location_repr = {"title": "Steve makes epic jump on bike", "excerpt": "Yo dog", "source": "BBC News",
    #                     "location": "", "pubDate": "2016-10-17T12:35:12Z", "author": "BBC News"}
    #     a = Article(**article_repr)
    #     self.session.add(a)

    #     r = self.session.query(Article).filter(Article.title == "Steve makes epic jump on bike").first()
    #     self.assertEqual(r.excerpt, "Yo dog")
    #     self.assertEqual(r.source, "BBC News")
    #     self.assertEqual(r.location, "")
    #     self.assertEqual(r.pubDate, "2016-10-17T12:35:12Z")
    #     self.assertEqual(r.author, "BBC News")

    # def test_article_insert_2(self):
    #     location_repr = {"title": "In deep-red Florida, signs of trouble for Donald Trump", 
    #         "excerpt": "Some residents of The Villages, a GOP stronghold in Florida, are so disgusted with Donald Trump that they're backing Hillary Clinton for president.",
    #         "source": "USA Today",
    #         "location": "", 
    #         "pubDate": "2016-10-17T12:20:39Z", 
    #         "author": "Ledyard King"}
    #     a = Article(**article_repr)
    #     self.session.add(a)

    #     r = self.session.query(Article).filter(Article.title == "Steve makes epic jump on bike").first()
    #     self.assertEqual(r.title, "In deep-red Florida, signs of trouble for Donald Trump")
    #     self.assertEqual(r.excerpt, "Some residents of The Villages, a GOP stronghold in Florida, are so disgusted with Donald Trump that they're backing Hillary Clinton for president.")
    #     self.assertEqual(r.source, "USA Today")
    #     self.assertEqual(r.location, "")
    #     self.assertEqual(r.pubDate, "2016-10-17T12:20:39Z")
    #     self.assertEqual(r.author, "Ledyard King")

    # def test_article_insert_3(self):
    #     location_repr = {"title": "Official: Icardi remains Inter captain", 
    #         "excerpt": "Mauro Icardi “will be sanctioned” by Inter, but the striker will not be stripped of the captaincy.", 
    #         "source": "Football Italia",
    #         "location": "", 
    #         "pubDate": "2016-10-17T01:00:00Z", 
    #         "author": "Football Italia Staff"}
    #     a = Article(**article_repr)
    #     self.session.add(a)

    #     r = self.session.query(Article).filter(Article.title == "Official: Icardi remains Inter captain").first()
    #     self.assertEqual(r.excerpt, "Mauro Icardi “will be sanctioned” by Inter, but the striker will not be stripped of the captaincy.")
    #     self.assertEqual(r.source, "Football Italia")
    #     self.assertEqual(r.location, "")
    #     self.assertEqual(r.pubDate, "2016-10-17T01:00:00Z")
    #     self.assertEqual(r.author, "Football Italia Staff")

if __name__ == '__main__':
<<<<<<< HEAD
    unittest.main()
=======
    app_instance.config["TESTING"] = True
    app_instance.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('BESTBYTES_DB_TEST')
    # db.create_all()
    unittest.main()
    # db.drop_all()
>>>>>>> e6c0cc06fc04e03b9b174712a31a056f53822d48
