from flask import Flask, render_template,jsonify
import requests

app = Flask(__name__)

def get_meme():
    title = ""
    image = ""
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    data  = response.json()
    title = data['title']
    image = data["preview"][2]
    return (title, image)

@app.route("/")
def index():
    title, image_url = get_meme()
    return render_template('index.html', title = title, image_url = image_url)

@app.route("/get_meme")
def send_meme():
    title, img = get_meme()
    data = {
        'title' : title,
        'img' : img
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)