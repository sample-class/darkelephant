from flask import Flask
from flask import render_template
from flask import request
import mok
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    page = render_template("index.html", mok=mok)
    return page

@app.route('/from/<direction>')
def from_to(direction):
    tours = {x:mok.tours[x] for x in mok.tours if mok.tours[x]['departure'] == direction}
    min_max = {}
    min_max['min_price'] = min([tours[tour]['price'] for tour in tours])
    min_max['max_price'] = max([tours[tour]['price'] for tour in tours])
    min_max['min_nights'] = min([tours[tour]['nights'] for tour in tours])
    min_max['max_nights'] = max([tours[tour]['nights'] for tour in tours])
    page = render_template("direction.html", direction=direction, mok=mok, filter_tours=tours, min_max = min_max)
    return page

@app.route('/tours/<id>')
def about(id):
    page = render_template("tour.html", id=id, mok=mok)
    return page

if __name__ == "__main__":
    app.run('localhost', 8000)
    