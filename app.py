import flask
import game_of_life

app = flask.Flask(__name__)


@app.route("/")
def index():
    game_of_life.GameOfLife(25,25)
    return flask.render_template("index.html")


@app.route("/live")
def live():
    live = game_of_life.GameOfLife()
    
    res = flask.render_template("live.html", live=live)
    live.form_new_generation()
    return res

if __name__ == "__main__":
    app.run( host="127.0.0.1", port=8888 )

