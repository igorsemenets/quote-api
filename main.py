from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It always seems impossible until it's done."
]

@app.route('/')
def home():
    return '''
    <h1>Quote API</h1>
    <p>Welcome to the Quote API. Use <code>/quote</code> to get a random quote.</p>
    '''

@app.route('/quote')
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

@app.route('/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
