import flask
import get_files

app = flask.Flask("__main__")
@app.route('/')

def my_index():
    return flask.render_template("index.html",token="HelloFlask+React")

app.run(debug=True)