from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello cs373f"

@app.route('/books')
def books():
    return "This is the books page"

if __name__ == "__main__":
    app.run()
