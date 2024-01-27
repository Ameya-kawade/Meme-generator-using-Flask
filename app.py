from flask import Flask, render_template,jsonify
import requests
from random import randint

app = Flask(__name__)

def get_meme():
    memes = ['memes', 'dankmemes', 'me_irl','wholesomememes']
    title = ""
    image = ""
    url = f"https://meme-api.com/gimme/{memes[randint(0,len(memes) - 1)]}"
    response = requests.get(url)
    if response.status_code == 200:
        data  = response.json()
        title = data['title']
        image = data["preview"][2]
    else:
        title = "Meme not found"
        image = ""    
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
    app.run(debug = True)
