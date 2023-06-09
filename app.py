from flask import Flask, Response, render_template
import lichess.api
from dotenv import load_dotenv
import os

load_dotenv()

def rating(time_control):
    username = os.getenv("username")
    user = lichess.api.user(username)
    return user['perfs'][time_control]['rating']

def generate_card(time_control):
    elo = rating(time_control)
    if time_control == "blitz":
        time_control = "Lichess Blitz"
    elif time_control == "rapid":
        time_control = "Lichess Rapid"
    elif time_control == "bullet":
        time_control = "Lichess Bullet"

    svg = render_template(
        "card.html.j2",
        time_control = time_control,
        elo = elo
    )
    return svg

app = Flask(__name__)

@app.route("/")
def handle_all():
    time_control = os.getenv("time_control")
    svg = generate_card(time_control)
    resp = Response(svg, mimetype="image/svg+xml")
    resp.headers["Cache-Control"] = "s-maxage=1"        
    return resp

if __name__ == "__main__":
    app.run(debug=True)