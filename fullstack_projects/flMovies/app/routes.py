from app import app
from flask import render_template, flash, redirect, url_for, request
from app import db
from app.models import Movie

@app.route('/', methods = ['POST','GET'])
@app.route('/index',methods = ['POST','GET'])
def index():
    movies = None
    if request.method == "POST":
        title = request.form['search']
        movies = Movie.query.filter(Movie.title.contains(title)).order_by(Movie.title).all()
        return render_template("index.html",movies = movies)
    else:
        movies = Movie.query.all()
        return render_template('index.html', movies = movies)

@app.route('/view/<int:id>')
def view_movie(id):
	my_data = Movie.query.get(id)
	return render_template("view_movie.html", movie = my_data)

@app.route('/add/', methods=["GET", "POST"])
def add_movie():
	if request.method == "POST":
		title = request.form['title']
		price = request.form['price']
		genre = request.form['genre']
		release_date = request.form['release_date']
		my_data = Movie(title, genre, release_date, price)
        #title, genre, release_date, price
		db.session.add(my_data)
		db.session.commit()
		flash("Movie Added succesfully")
		return redirect(url_for('index'))
	return render_template('add_movie.html')


@app.route('/edit/<int:id>',methods = ['GET', 'POST'])
def edit_movie(id):
	if request.method == "POST":
		my_data = Movie.query.get(id)
		my_data.title = request.form['title']
		my_data.price = request.form['price']
		my_data.genre = request.form['genre']
		my_data.release_date = request.form['release_date']
		db.session.commit()
		flash("Movie updated succesfully")
		return redirect(url_for("index"))
	else:
		movie = Movie.query.get(id)
		return render_template("edit_movie.html", movie = movie)


@app.route("/delete/<int:id>")
def delete_movie(id):
	my_data = Movie.query.get(id)
	db.session.delete(my_data)
	db.session.commit()
	flash("Movie Deleted succesfully")
	return redirect(url_for("index"))