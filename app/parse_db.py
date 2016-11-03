import json
from app import db, app_instance
from models import Article, Source, Location

def parse_sources():
	with open("../data/api_data/final_data/final_sources.json") as f:
		src_json = json.load(f);
	
	for src in src_json:
		s = Source(id_num=src['id_num'], id_name=src['id_name'], language=src['language'], \
			description=src['description'], smallLogoURL=src['smallLogoURL'], mediumLogoURL=src['mediumLogoURL'], \
			largeLogoURL=src['largeLogoURL'], category=src['category'], external_link=src['external_link'],name=src['name'],\
			region=src['region'], country=src['country'])
		db.session.add(s)
		print("Source " + s.id_num + " added to db")

	db.session.commit()
	print("Sources Committed")


def parse_locations():
	with open("../data/api_data/final_data/final_locations.json") as f:
		loc_json = json.load(f);

	for loc in loc_json:
		l = Location(id_num=loc['id_num'], currencies=loc['currencies'], \
			latlng=loc['latlng'], capital=loc['capital'], population=loc['population'], \
			topLevelDomain=loc['topLevelDomain'], languages=loc['languages'], \
			name=loc['name'], region=loc['region'])
		db.session.add(l)
		print("Location " + l.id_num + " added to db")

	db.session.commit()
	print("Locations Committed")	


def parse_articles():
	with open('../data/api_data/final_data/final_articles.json', 'r') as f:
		art_json = json.load(f);

	for art in art_json:
		a = Article(id_num=art['id_num'], title=art['title'], description=art['description'], \
			pubDate=art['pubDate'], image_link=art['image_link'], category=art['category'], \
			external_article_link=art['external_article_link'], external_source_link=art['external_source_link'], \
			source_name=art['source_name'], region=art['region'])
		db.session.add(a)
		print("Article " + a.id_num + " added to db")

	db.session.commit()
	print("Articles Committed")


# Drop all tables and recreate empty
db.reflect()
db.drop_all()
db.create_all()

parse_sources()
parse_locations()
parse_articles()
db.session.close()
