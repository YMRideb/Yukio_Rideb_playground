from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!!'


# def level_1():
#     return render_template("index.html")


@app.route('/play')
@app.route('/play/<int:x>/<string:color>')
def level_2(x=3, color='aquamarine'):
    return render_template("level_2.html", x=x, color=color)

if __name__ == "__main__":
    app.run(debug=True)
