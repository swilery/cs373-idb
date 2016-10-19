import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

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

@app.route('/single')
def single():
    return render_template('single.html')

@app.route('/location_page')
def location_page():
    return render_template('location_page.html')

@app.route('/source_page')
def source_page():
    return render_template('source_page.html')

if __name__ == "__main__":
	with open('../data/api_data/sample_articles.json', 'r') as f:
		articles = json.load(f)
	with open('../data/api_data/sample_sources.json', 'r') as f:
		sources = json.load(f)
	with open('../data/api_data/sample_countries.json', 'r') as f:
		countries = json.load(f)

	app.run()
