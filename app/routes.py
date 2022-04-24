from flask import Flask, render_template, redirect, url_for, request
from app.parser import ParsPage
from config import SAVE_FOLDER
from app.urlvalidator import url_check


def init_routes(app: Flask):
    @app.get('/')
    def index():
        return redirect(url_for('parser'))

    @app.route('/parser', methods=['GET', 'POST'])
    def parser():
        urls = []
        if request.method == 'POST':
            url = request.form.get('Url')
            result = url_check(url)
            if result[0] is True:
                img = ParsPage(**result[1], save_directory=SAVE_FOLDER)
                img.get_imgs_data()
                img.save_imgs()
                urls = img.path_to_imgs
            else:
                exception = result[1]
                return render_template("parser.html", exception=exception)
        return render_template("parser.html", urls=urls)

    @app.get('/about')
    def about():
        return render_template("about.html")
