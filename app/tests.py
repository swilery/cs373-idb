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
    def test_article_insert_1(self):
        a = Article(id_num='5000', title='Ben Needham killed in accident', description='Toddler Ben Needham died as a result of an accident near where he was last seen on the Greek island of Kos in 1991, police believe.', \
        pubDate='2016-10-17', image_link='http://ichef-1.bbci.co.uk/news/1024/cpsprodpb/3AA4/production/_91221051_mediaitem89648446.jpg', category='General', \
        external_article_link='http://www.bbc.co.uk/news/uk-england-37676268', external_source_link='http://www.bbc.com/news', \
        source_name='BBC News', region='Great Britain')
        db.session.add(a)
        db.session.commit()

        r = db.session.query(Article).filter(Article.title == 'Ben Needham killed in accident').first()
        self.assertEqual(r.id_num, '5000')
        self.assertEqual(r.title, 'Ben Needham killed in accident')
        self.assertEqual(r.description, 'Toddler Ben Needham died as a result of an accident near where he was last seen on the Greek island of Kos in 1991, police believe.')
        self.assertEqual(r.pubDate, '2016-10-17')
        self.assertEqual(r.image_link, 'http://ichef-1.bbci.co.uk/news/1024/cpsprodpb/3AA4/production/_91221051_mediaitem89648446.jpg')
        self.assertEqual(r.category, 'General')
        self.assertEqual(r.external_article_link, 'http://www.bbc.co.uk/news/uk-england-37676268')
        self.assertEqual(r.external_source_link, 'http://www.bbc.com/news')
        self.assertEqual(r.source_name, 'BBC News')
        self.assertEqual(r.region, 'Great Britain')

        db.session.query(Article).filter(Article.title == 'Ben Needham killed in accident').delete()
        db.session.commit()

    def test_article_insert_2(self):
        a = Article(id_num='5001', title='Title', description='Flying Pigs Invade Russia', \
        pubDate='2016-11-2', image_link='pigs.jpg', category='Crazy', \
        external_article_link='http://www.three_little_pigs.me', external_source_link='http://www.gdc.edu', \
        source_name='rfuller250', region='UTCS')
        db.session.add(a)
        db.session.commit()

        r = db.session.query(Article).filter(Article.description == 'Flying Pigs Invade Russia').first()
        self.assertEqual(r.id_num, '5001')
        self.assertEqual(r.title, 'Title')
        self.assertEqual(r.description, 'Flying Pigs Invade Russia')
        self.assertEqual(r.pubDate, '2016-11-2')
        self.assertEqual(r.image_link, 'pigs.jpg')
        self.assertEqual(r.category, 'Crazy')
        self.assertEqual(r.external_article_link, 'http://www.three_little_pigs.me')
        self.assertEqual(r.external_source_link, 'http://www.gdc.edu')
        self.assertEqual(r.source_name, 'rfuller250')
        self.assertEqual(r.region, 'UTCS')

        db.session.query(Article).filter(Article.description == 'Flying Pigs Invade Russia').delete()
        db.session.commit()

    def test_article_insert_3(self):
        a = Article(id_num='5002', title='President Trump Launches Nuclear Strike Against Canada', description='We are all gonna die! :(', \
        pubDate='2016-11-9', image_link='mushroom_cloud.gif', category='Death', \
        external_article_link='http://www.armageddon.me', external_source_link='http://www.i_miss_obama.gov', \
        source_name='swilery', region='HELL!')
        db.session.add(a)
        db.session.commit()

        r = db.session.query(Article).filter(Article.region == 'HELL!').first()
        self.assertEqual(r.id_num, '5002')
        self.assertEqual(r.title, 'President Trump Launches Nuclear Strike Against Canada')
        self.assertEqual(r.description, 'We are all gonna die! :(')
        self.assertEqual(r.pubDate, '2016-11-9')
        self.assertEqual(r.image_link, 'mushroom_cloud.gif')
        self.assertEqual(r.category, 'Death')
        self.assertEqual(r.external_article_link, 'http://www.armageddon.me')
        self.assertEqual(r.external_source_link, 'http://www.i_miss_obama.gov')
        self.assertEqual(r.source_name, 'swilery')
        self.assertEqual(r.region, 'HELL!')

        db.session.query(Article).filter(Article.region == 'HELL!').delete()
        db.session.commit()

    # Insert location
    def test_location_insert_1(self):
        l = Location(id_num='500', currencies='beans', \
            latlng='42,42', capital='Dot', population='0', \
            topLevelDomain='period_dot.com', languages='weird', \
            name='0D', region='None')
        db.session.add(l)
        db.session.commit()

        r = db.session.query(Location).filter(Location.currencies == "beans").first()
        self.assertEqual(r.id_num, '500')
        self.assertEqual(r.currencies, 'beans')
        self.assertEqual(r.latlng, '42,42')
        self.assertEqual(r.capital, 'Dot')
        self.assertEqual(r.population, '0')
        self.assertEqual(r.topLevelDomain, 'period_dot.com')
        self.assertEqual(r.languages, 'weird')
        self.assertEqual(r.name, '0D')
        self.assertEqual(r.region, 'None')

        db.session.query(Location).filter(Location.currencies == 'beans').delete()
        db.session.commit()

    # Insert location
    def test_location_insert_2(self):
        l = Location(id_num='501', currencies='puppies', \
            latlng='12,45', capital='Carac', population='31', \
            topLevelDomain='pudding.com', languages='English', \
            name='Frec', region='Mordor')
        db.session.add(l)
        db.session.commit()

        r = db.session.query(Location).filter(Location.capital == "Carac").first()
        self.assertEqual(r.id_num, '501')
        self.assertEqual(r.currencies, 'puppies')
        self.assertEqual(r.latlng, '12,45')
        self.assertEqual(r.capital, 'Carac')
        self.assertEqual(r.population, '31')
        self.assertEqual(r.topLevelDomain, 'pudding.com')
        self.assertEqual(r.languages, 'English')
        self.assertEqual(r.name, 'Frec')
        self.assertEqual(r.region, 'Mordor')

        db.session.query(Location).filter(Location.capital == "Carac").delete()
        db.session.commit()

        # Insert location
    def test_location_insert_3(self):
        l = Location(id_num='502', currencies='Death', \
            latlng='34,22', capital='Zombia', population='206', \
            topLevelDomain='sync.com', languages='jargon', \
            name='Threads', region='OS')
        db.session.add(l)
        db.session.commit()

        r = db.session.query(Location).filter(Location.languages == "jargon").first()
        self.assertEqual(r.id_num, '502')
        self.assertEqual(r.currencies, 'Death')
        self.assertEqual(r.latlng, '34,22')
        self.assertEqual(r.capital, 'Zombia')
        self.assertEqual(r.population, '206')
        self.assertEqual(r.topLevelDomain, 'sync.com')
        self.assertEqual(r.languages, 'jargon')
        self.assertEqual(r.name, 'Threads')
        self.assertEqual(r.region, 'OS')

        db.session.query(Location).filter(Location.languages == "jargon").delete()
        db.session.commit()


if __name__ == '__main__':
    unittest.main()
