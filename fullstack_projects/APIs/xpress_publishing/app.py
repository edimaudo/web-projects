from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Artist, Series, Issue

# Connect to Database and create database session
engine = create_engine('sqlite:///xpress_publishing.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



#artist
#/api/artists
@app.route('/artists')
def showArtists():
	artists = session.query(Artist).all()
	return render_template('books.html', artists=artists)

#/api/artists
#If any required fields are missing, returns a 400 response
@app.route('/artist/new/', methods=['GET', 'POST'])
def newArtist():
    if request.method == 'POST':
        newArtist = Book(artist_name=request.form['artist_name'],
                       date_of_birth=request.form['date_of_birth'],
                       biography=request.form['biography'],
                       is_currently_employed=request.form['s_currently_employed'])
        session.add(newArtist)
        session.commit()
        return redirect(url_for('showArtists'))
    else:
        return render_template('newArtist.html')


def get_artists():
    artists = session.query(Artist).all()
    return jsonify(books=[a.serialize for a in artists])	

#API routing
@app.route('/artistApi', methods=['GET', 'POST'])
def artistFunction():
    if request.method == 'GET':
        return get_books()
    elif request.method == 'POST':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return makeANewBook(title, author, genre)


@app.route('/booksApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def bookFunctionId(id):
    if request.method == 'GET':
        return get_book(id)

    elif request.method == 'PUT':
        title = request.args.get('title', '')
        author = request.args.get('author', '')
        genre = request.args.get('genre', '')
        return updateBook(id, title, author, genre)

    elif request.method == 'DELETE':
        return deleteABook(id)

#/api/artists/:artistId
#GET
#Returns a 200 response containing the artist with the supplied artist ID on the artist property of the response body
#If an artist with the supplied artist ID doesn't exist, returns a 404 response


#/api/artists/:artistId
#PUT
#Updates the artist with the specified artist ID using the information from the artist property of the request body and 
#saves it to the database. 
#Returns a 200 response with the updated artist on the artist property of the response body
#If any required fields are missing, returns a 400 response
#If an artist with the supplied artist ID doesn't exist, returns a 404 response

#DELETE
#Updates the artist with the specified artist ID to be unemployed (is_currently_employed equal to 0). 
#Returns a 200 response.
#If an artist with the supplied artist ID doesn't exist, returns a 404 response