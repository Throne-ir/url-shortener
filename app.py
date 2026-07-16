from flask import Flask, request, redirect
import string
import random

app = Flask(__name__)
url_map = {}

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/')
def home():
    return """
    <h1>URL Shortener</h1>
    <form action="/shorten" method="post">
        <input type="url" name="url" placeholder="Enter long URL" required>
        <button type="submit">Shorten</button>
    </form>
    """

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['url']
    short_code = generate_short_code()
    url_map[short_code] = long_url
    return f"Short URL: http://localhost:5000/{short_code}"

@app.route('/<short_code>')
def redirect_url(short_code):
    long_url = url_map.get(short_code)
    if long_url:
        return redirect(long_url)
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
