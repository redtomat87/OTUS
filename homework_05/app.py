"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""

from flask import Flask, request, render_template

from views.items import items_app
from views.products import products_app

app = Flask(__name__)
app.register_blueprint(
    items_app,
    # url_prefix="/items",
)
app.register_blueprint(
    products_app,
)


@app.get("/", endpoint="index")
def index():
    return render_template("index.html")


@app.get("/about/", endpoint="about")
def about():
    return render_template("about.html")


@app.route("/hello/")
@app.get("/hello/<name>/")
def hello_path_view(name: str | None = None):
    print(request)
    if name is None:
        name = request.args.get("name", "")
    name = name.strip()
    if not name:
        name = "World"
    return {"message": f"Hello, {name}!"}


if __name__ == "__main__":
    app.run(debug=True)
