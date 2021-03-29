from flask import Flask, render_template, request, redirect, url_for

from forms import *
from models import *

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route('/')
def home():
    return render_template("home.html")


@app.route("/films/", methods = ["GET","POST"])
def films_page():
    form = FilmForm()
    if request.method == "POST":
        if form.validate_on_submit():
            films.create(form.data)
            return redirect('/films')

    return render_template("films.html", films=films.all(), form=form)


@app.route("/films/<int:film_id>", methods = ["GET","POST"])
def detail(film_id):
    film = films.get(film_id)
    comments_id = film["comments_id"]
    form = FilmForm(data=film)
    comments = films.show_comments(film_id)
    #memory.remember_id(film_id)

    if request.method == "POST":
        if form.validate_on_submit():
            films.update(film_id, form.data, comments_id)
        return redirect(url_for("films_page"))
    return render_template("film.html", film_id=film_id, film=film, form=form, comments=comments)


@app.route("/films/<int:film_id>/delete", methods = ["GET","POST"])
def delete(film_id):
    if request.method == "POST":
        films.delete(film_id)
        return redirect(url_for("films_page"))

    return render_template("delete.html", film_id=film_id)


@app.route("/films/<int:film_id>/comments", methods = ["GET","POST"])
def comments_page(film_id):
    form = CommentForm()
    data = request.form

    if request.method == "POST":
        films.create_comment(film_id, data)
        return redirect(f"/films/{film_id}")

    return render_template("komentarz.html", film_id=film_id, form=form )



if __name__ == "__main__":
    app.run(debug=True)