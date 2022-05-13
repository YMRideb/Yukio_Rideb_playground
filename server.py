from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/play')
def level_1():
    return render_template("index.html")


@app.route('/play/<int:x>/<string:color>')
def level_2(x, color):
    return render_template("level_2.html", x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)
