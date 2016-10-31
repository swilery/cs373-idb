import json
from app import db, app_instance
from models import Article, Source, Location
from pprint import pprint

def parse_sources():
	with open("../data/api_data/final_data/final_sources.json") as f:
		src_json = json.load(f);
	
	for src in src_json:
		s = Source(id_num=src['id_num'], id_name=src['id_name'], language=src['language'], \
			description=src['description'],urlsToLogos=str(src['urlsToLogos']), \
			category=src['category'], external_link=src['external_link'],name=src['name'],\
			region=src['region'], country=src['country'])
		db.session.add(s)
		print("Source " + s.id_num + " added to db")

	db.session.commit()
	print("Sources Committed")


def parse_locations():
	with open("../data/api_data/final_data/final_locations.json") as f:
		loc_json = json.load(f);

	for loc in loc_json:
		l = Location(id_num=loc['id_num'], currencies=str(loc['currencies']), \
			latlng=str(loc['latlng']), capital=loc['capital'], population=loc['population'], \
			topLevelDomain=str(loc['topLevelDomain']), languages=str(loc['languages']), \
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
			source_name=['source_name'], region=['region'])
		db.session.add(a)
		print("Article " + a.id_num + " added to db")

	db.session.commit()
	print("Articles Committed")


db.session.commit()
parse_sources()
parse_articles()
parse_locations()
db.session.close()