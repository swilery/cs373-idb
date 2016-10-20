import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
	return render_template('articles.html', articles=articles)

@app.route('/sources')
def sources():
    return render_template('sources.html', sources=sources)

@app.route('/locations')
def locations():
    return render_template('locations.html', countries=countries)

@app.route('/article/<articleNum>')
def single(articleNum):
    articleNum = int(articleNum)-1
    return render_template('single.html', article=articles[articleNum])

@app.route('/location/<locationNum>')
def location_page(locationNum):
    locationNum = int(locationNum)-1
    mapRequest1 = "https://www.google.com/maps/embed/v1/place?q="
    mapRequest2 = "&key=AIzaSyDr7OP343FI-sez_S9hS4K2iL7Ii5l9_cs"
    name = countries[locationNum]["name"].replace(" ", "+")
    mapRequestFinal = mapRequest1 + name + mapRequest2
    return render_template('location_page.html', country=countries[locationNum], mapRequest=mapRequestFinal)

@app.route('/source/<sourceNum>')
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

	app.run()
