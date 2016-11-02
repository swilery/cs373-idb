import json
from loader import app_instance, db
from flask import render_template, jsonify, make_response, abort
from models import Article, Source, Location
from random import randint

# -----------------------
# Web Application Routing
# -----------------------

@app_instance.route('/')
@app_instance.route('/index')
def index():
    numArticles = db.session.query(Article).count()
    num1 = randint(1, numArticles//3)
    num2 = randint(numArticles//3, numArticles//3*2)
    num3 = randint(numArticles//3*2, numArticles)
    article1 = Article.query.filter_by(id_num=str(num1)).first()
    article2 = Article.query.filter_by(id_num=str(num2)).first()
    article3 = Article.query.filter_by(id_num=str(num3)).first()
    return render_template('index.html', article1=article1, article2=article2, article3=article3)


@app_instance.route('/unittests')
def tests():
    from subprocess import getoutput
    from os import path
    p = path.join(path.dirname(path.realpath(__file__)), 'tests.py')
    output = getoutput('python3 '+p)
    print(output)
    return jsonify({'output': str(output)})    

@app_instance.route('/about')
def about():
    return render_template('about.html')

@app_instance.route('/articles')
def articles():
	articles = Article.query.paginate(1, 50, False).items
	return render_template('articles.html', articles=articles)

@app_instance.route('/sources')
def sources():
    sources = db.session.query(Source).all()
    return render_template('sources.html', sources=sources)

@app_instance.route('/locations')
def locations():
    locations = db.session.query(Location).all()
    return render_template('locations.html', locations=locations)

@app_instance.route('/article/<articleNum>')
def single(articleNum):
    article = Article.query.filter_by(id_num=articleNum).first()
    source = Source.query.filter_by(name=article.source_name).first()
    locations = Location.query.filter_by(region=article.region).all()
    return render_template('single.html', article=article, source=source, locations=locations)

@app_instance.route('/location/<locationNum>')
def location_page(locationNum):
    location = Location.query.filter_by(id_num=locationNum).first()
    sources = Source.query.filter_by(country=location.name).all()
    articles = Article.query.filter_by(region=location.region).all()
    mapRequest1 = "https://www.google.com/maps/embed/v1/place?q="
    mapRequest2 = "&key=AIzaSyDr7OP343FI-sez_S9hS4K2iL7Ii5l9_cs"
    wikiRequest1 = "https://en.wikipedia.org/wiki/"
    mapName = (location.name).replace(" ", "+")
    wikiName = (location.name).replace(" ", "_")
    mapRequestFinal = mapRequest1 + mapName + mapRequest2
    wikiRequestFinal = wikiRequest1 +wikiName
    return render_template('location_page.html', location=location, sources=sources, articles=articles, \
    mapRequest=mapRequestFinal, wikiRequest=wikiRequestFinal)

@app_instance.route('/source/<sourceNum>')
def source_page(sourceNum):
    source = Source.query.filter_by(id_num=sourceNum).first()
    articles = Article.query.filter_by(source_name=source.name).all()
    location = Location.query.filter_by(name=source.country).first()
    return render_template('source_page.html', source=source, articles=articles, location=location)
    
    
# -----------
# RESTful API
# -----------

# Returns all data in json format
@app_instance.route('/api/all', methods=['GET'])
def get_all():
   articles = Article.query.all()
   sources = Source.query.all()
   locations = Location.query.all()
   data = { }
   data['articles'] = [article.to_json() for article in articles]
   data['sources'] = [source.to_json() for source in sources]
   data['locations'] = [location.to_json() for location in locations]
   return jsonify(data)

# Returns all articles in json format
@app_instance.route('/api/articles/all', methods=['GET'])
def get_articles_all():
   articles = Article.query.all()
   return jsonify({'articles': [article.to_json() for article in articles]})

# Returns 50 articles in json format, change page number at end of url to access more articles
@app_instance.route('/api/articles', methods=['GET'])
@app_instance.route('/api/articles/page=<int:page>', methods=['GET'])
def get_articles(page=1):
   articles = Article.query.paginate(page=page, per_page=50).items
   return jsonify({'articles': [article.to_json() for article in articles]})
   
# Returns article with id_num in json format
@app_instance.route('/api/articles/id=<string:id_num>', methods=['GET'])
def get_article(id_num=1):
   article = Article.query.filter_by(id_num=id_num).first()
   if article is None:
      abort(404)
   return jsonify(article.to_json())
   
# Returns all sources in json format
@app_instance.route('/api/sources/all', methods=['GET'])
def get_sources_all():
   sources = Source.query.all()
   return jsonify({'sources': [source.to_json() for source in sources]})
   
# Returns 25 sources in json format, change page number at end of url to access more sources
@app_instance.route('/api/sources', methods=['GET'])
@app_instance.route('/api/sources/page=<int:page>', methods=['GET'])
def get_sources(page=1):
   sources = Source.query.paginate(page=page, per_page=25).items
   return jsonify({'sources': [source.to_json() for source in sources]})
   
# Returns source with id_num in json format
@app_instance.route('/api/sources/id=<string:id_num>', methods=['GET'])
def get_source(id_num=1):
   source = Source.query.filter_by(id_num=id_num).first()
   if source is None:
      abort(404)
   return jsonify(source.to_json())
   
# Returns all locations in json format
@app_instance.route('/api/locations/all', methods=['GET'])
def get_locations_all():
   locations = Location.query.all()
   return jsonify({'locations': [location.to_json() for location in locations]})
   
# Returns 25 locations in json format, change page number at end of url to access more sources
@app_instance.route('/api/locations', methods=['GET'])
@app_instance.route('/api/locations/page=<int:page>', methods=['GET'])
def get_locations(page=1):
   locations = Location.query.paginate(page=page, per_page=25).items
   return jsonify({'locations': [location.to_json() for location in locations]})
   
# Returns location with id_num in json format
@app_instance.route('/api/locations/id=<string:id_num>', methods=['GET'])
def get_location(id_num=1):
   location = Location.query.filter_by(id_num=id_num).first()
   if location is None:
      abort(404)
   return jsonify(location.to_json())

# Returns error json 
@app_instance.errorhandler(404)
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
	app_instance.run()
