#!/usr/bin/env python3

import json
import requests

# Pull articles from News API & Newslookup API
def getAllArticles():
   getNewsAPIArticles()
   getNewslookupArticles()


# News API
# Pulls all articles for all sources
# Format: {source_id:[articles_list]}
def getNewsAPIArticles():
   with open('api_data/news_api_sources_id_map.json', 'r') as f:
      source_map = json.load(f)
      
   apiKey = '836d24a3cd7c43bd9450a4496c2dbf41'
   url_part1 = 'https://newsapi.org/v1/articles?source='
   url_part2 = '&apiKey=' + apiKey

   allArticles = { }
   for source in source_map.keys():
      response = requests.get(url_part1 + source + url_part2)
      response = response.json()
      articles = response['articles']
      allArticles[source] = articles
      
   with open('api_data/news_api_all_articles.json', 'w') as f:
      json.dump(allArticles, f)

# Newslookup API
# Pulls all articles for all regions
# Format: {region:[articles_list]}
def getNewslookupArticles():
	with open('api_data/newslookup_regions_id_map.json', 'r') as f:
		region_map = json.load(f)

	client_id = '17122'
	secret = '32c77c1b83556dbf3c621247302af153'
	url_part1 = 'https://api.newslookup.com/feed/live?fmt=&region='
	url_part2 = '&output=json&client_id='
	url_part3 = '&secret='

	allArticles = { }
	for region in region_map.keys():
		response = requests.get(url_part1 + region + url_part2 + client_id + url_part3 + secret)
		response = response.json()
		articles = response['items']
		allArticles[region_map[region]] = articles

	with open('api_data/newslookup_api_all_articles.json', 'w') as f:
		json.dump(allArticles, f)


# Temporary
# Pulls 3 specific articles, sources, and locations
def getSampleData():
	with open('api_data/news_api_all_articles.json', 'r') as f:
		articles = json.load(f)

	with open('api_data/news_api_sources.json', 'r') as f:
		sources = (json.load(f))['sources']

	with open('api_data/rest_countries_all.json', 'r') as f:
		countries = json.load(f)

	article1 = articles['bbc-news'][0]
	article1['source'] = 'BBC News'
	article2 = articles['usa-today'][0]
	article2['source'] = 'USA Today'
	article3 = articles['football-italia'][0]
	article3['source'] = 'Football Italia'

	source1 = { }
	source2 = { }
	source3 = { }
	for source in sources:
		if source['id'] == 'bbc-news':
			source1 = source
		if source['id'] == 'usa-today':
			source2 = source
		if source['id'] == 'football-italia':
			source3 = source

	country1 = { }
	country2 = { }
	country3 = { }
	for country in countries:
		if country['alpha2Code'] == 'GB':
			country1 = country
		if country['alpha2Code'] == 'IT':
			country2 = country
		if country['alpha2Code'] == 'US':
			country3 = country

	sample_articles = [article1, article2, article3]
	sample_sources = [source1, source2, source3]
	sample_countries = [country1, country2, country3]

	with open('api_data/sample_articles.json', 'w') as f:
		json.dump(sample_articles, f)

	with open('api_data/sample_sources.json', 'w') as f:
		json.dump(sample_sources, f)

	with open('api_data/sample_countries.json', 'w') as f:
		json.dump(sample_countries, f)

if __name__ == '__main__':
   # getAllArticles()
   getSampleData()