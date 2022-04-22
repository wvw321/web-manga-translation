from flask import Flask, render_template, redirect, url_for, request


def init_routes(app: Flask):
    @app.get('/')
    def index():
        return redirect(url_for('parser'))

    @app.route('/parser', methods=['GET', 'POST'])
    def parser():
        urls = []
        if request.method == 'POST':
            ...
            # получаем ссылку
            # понимакм как скачать
            # выгружаем список
            # загружаем в базу / папку
            # перевод
            # urls на новые

        return render_template("parser.html", urls=urls)

    @app.get('/about')
    def about():
        return render_template("about.html")
