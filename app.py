from flask import Flask, render_template, request
from parser_img import ParsPage

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        a = request.form.get('Url')
        print(a)

    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
