import json
from app import db, app_instance
from app import Article, Source, Location
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
		print(s.id_name + " added to db")

	db.session.commit()
	print("Sources Committed")

	r = db.session.query(Source).filter(Source.id_name == "usa-today").first()
	print(r.name)
	print(r.region)
	print(r.category)
	print(r.description)
	# pprint(src_json)

def parse_locations():
	with open("../data/api_data/final_data/final_locations.json") as f:
		loc_json = json.load(f);

	pprint(loc_json)

def parse_articles():
	with open('../data/api_data/final_data/final_articles.json', 'r') as f:
		art_json = json.load(f);

	pprint(art_json)

parse_sources()