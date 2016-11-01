import json
from loader import app_instance, db
from flask import render_template
from models import Article, Source, Location
from random import randint

#from flask import Flask, render_template 
#from flask_sqlalchemy import SQLAlchemy

# app_instance = Flask(__name__)
# app_instance.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app_instance.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app_instance.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://162.243.14.196/postgresql'

# db = SQLAlchemy(app_instance)

#from models import Article, Source, Location

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
    articleNum = int(articleNum)-1
    return render_template('single.html', article=articles[articleNum])

@app_instance.route('/location/<locationNum>')
def location_page(locationNum):
    locationNum = int(locationNum)-1
    mapRequest1 = "https://www.google.com/maps/embed/v1/place?q="
    mapRequest2 = "&key=AIzaSyDr7OP343FI-sez_S9hS4K2iL7Ii5l9_cs"
    name = countries[locationNum]["name"].replace(" ", "+")
    mapRequestFinal = mapRequest1 + name + mapRequest2
    return render_template('location_page.html', country=countries[locationNum], mapRequest=mapRequestFinal)

@app_instance.route('/source/<sourceNum>')
def source_page(sourceNum):
    sourceNum = int(sourceNum)-1
    return render_template('source_page.html', source=sources[sourceNum], country=countries[sourceNum])

if __name__ == "__main__":
	with open('../data/api_data/sample_articles.json', 'r') as f:
		articles = json.load(f)
	with open('../data/api_data/sample_sources.json', 'r') as f:
		sources = json.load(f)
	with open('../data/api_data/sample_countries.json', 'r') as f:
		countries = json.load(f)

	app_instance.run()
