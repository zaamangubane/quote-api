from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    {"id": 1, "quote": "The best way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"id": 2, "quote": "Don't let yesterday take too much up of today.", "author": "Will Rogers"},
    {"id": 3, "quote": "It's not whether you get knocked down, it's whether you get up.", "author": "Vince Lombardi"},
    {"id": 4, "quote": "You can do whatever if you put your mind to it.", "author": "Unknown"},
    {"id": 5, "quote": "Education is the key to success.", "author": "Nelson Mandela"},
    {"id": 6, "quote": "If you don't like the road you're walking on, start paving another one.", "author": "Dolly Parton"},
    {"id": 7, "quote": "Life is what happens to us while we are busy making other plans.", "author": "Allen Saunders"},
    {"id": 8, "quote": "Everything you can imagine is real.", "author": "Pablo Picasso"},
    {"id": 9, "quote": "Life isn't about finding yourself. Life is about creating yourself.", "author": "George Bernard Show"},
    {"id": 10, "quote": "Doubt kills more dreams than failure ever will.", "author": "Suzy Kassem"},
    {"id": 11, "quote": "Nothing is impossible. The word itself says I'm possible!", "author": "Audrey Hepburn"},
    {"id": 12, "quote": "The bad news is time flies. The good news is you're the pilot.", "author": "Michael Altshuler"},
]

@app.route('/quotes', methods=['GET'])
def get_all_quotes():
    return jsonify(quotes)

@app.route('/quotes/random', methods=['GET'])
def get_random_quote():
    return jsonify(random.choice(quotes))

@app.route('/quotes/<int:id>', methods=['GET'])
def get_quote_by_id(id):
    quote = next((q for q in quotes if q["id"] == id), None)
    if quote:
        return jsonify(quote)
    return jsonify({"error": "Quote not found"}), 404

if __name__ == '_main_':
    app.run(debug=True)
 