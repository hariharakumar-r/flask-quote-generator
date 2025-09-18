from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def get_random_quote():
    try:
        response = requests.get('https://api.quotable.io/random')
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {'error': 'Could not fetch quote. Try again!'}

@app.route('/')
def index():
    quote_data = get_random_quote()
    return render_template('index.html', quote=quote_data)

@app.route('/get-quote')
def get_quote():
    quote_data = get_random_quote()
    return jsonify(quote_data)

if __name__ == '__main__':
    app.run(debug=True)