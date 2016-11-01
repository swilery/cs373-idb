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
	articles = Article.query.paginate(50, 50, False).items
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

if __name__ == "__main__":
	app_instance.run()
