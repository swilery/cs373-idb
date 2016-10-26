import json
from models import Article, Source, Location
from pprint import pprint

def parse_sources():
	with open("../data/api_data/final_data/final_sources.json") as f:
		src_json = json.load(f);
	
	for src in src_json:
		s = Source(id_num=src['id_num'], id_name=src['id_name'], language=src['language'], \
			description=src['description'],urlsToLogos=src['urlsToLogos'], \
			category=src['category'], external_link=src['external_link'],name=src['name'],\
			region=src['region'], country=src['country'])
		pprint(s)

	print("Sources done.")
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