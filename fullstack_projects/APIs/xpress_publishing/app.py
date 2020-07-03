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


#==============
#Artist html routing
#==============
@app.route('/artists')
def showArtists():
	artists = session.query(Artist).all()
	return render_template('books.html', artists=artists)

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

#==============
#Artist API functions
#==============
def get_artists():
    artists = session.query(Artist).all()
    return jsonify(books=[a.serialize for a in artists])	

def get_artist(artist_id):
	artists = session.query(Artist).filter_by(id=artist_id).one()
	#add check if id does not exist
	return jsonify(artists=artists.serialize)

def makeANewArtist(artist_name, date_of_birth, biography, is_currently_employed):
	addedArtist = Artist(artist_name = artist_name, date_of_birth = date_of_birth, biography = biography,
		is_currently_employed = is_currently_employed)
	session.add(addedArtist)
	session.commit()
	return jsonify(Artist=addedArtist.serialize)

def updateArtist(id, artist_name, date_of_birth, biography, is_currently_employed):
    updatedArtist = session.query(Book).filter_by(id=id).one()
    if not artist_name:
        updatedArtist.artist_name = artist_name
    if not date_of_birth:
        updatedArtist.date_of_birth = date_of_birth
    if not biography:
        updatedArtist.biography = biography
    if not is_currently_employed:
    	updatedArtist.is_currently_employed = is_currently_employed
    session.add(updatedArtist)
    session.commit()
    return 'Updated an Artist with id %s' % id

def deleteArtist(id):
    artistToDelete = session.query(Artist).filter_by(id=id).one()
    session.delete(artistToDelete)
    session.commit()
    return 'Removed Artist with id %s' % id

#==============
#Artist API routing
#==============
#/api/artists
@app.route('/artistApi', methods=['GET', 'POST'])
def artistFunction():
    if request.method == 'GET':
        return get_artists()
    elif request.method == 'POST':
        artist_name = request.args.get('artist_name', '')
        date_of_birth = request.args.get('date_of_birth', '')
        biography = request.args.get('biography', '')
        is_currently_employed = request.args.get('is_currently_employed','')
        return makeANewArtist(artist_name, date_of_birth, biography, is_currently_employed)

#/api/artists/:artistId
@app.route('/artistApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def artistFunctionId(id):
	#GET
#Returns a 200 response containing the artist with the supplied artist ID on the artist property of the response body

    #If an artist with the supplied artist ID doesn't exist, returns a 404 response
    if request.method == 'GET':
        return get_artist(id)

#/api/artists/:artistId
#PUT
#Updates the artist with the specified artist ID using the information from the artist property of the request body and 
#saves it to the database. 
#Returns a 200 response with the updated artist on the artist property of the response body
#If any required fields are missing, returns a 400 response
#If an artist with the supplied artist ID doesn't exist, returns a 404 response

    elif request.method == 'PUT':
    	artist_name = request.args.get('artist_name', '')
    	date_of_birth = request.args.get('date_of_birth', '')
    	biography = request.args.get('biography', '')
    	is_currently_employed = request.args.get('is_currently_employed','')
        return updateArtist(id, artist_name, date_of_birth, biography, is_currently_employed)

#DELETE
#Updates the artist with the specified artist ID to be unemployed (is_currently_employed equal to 0). 
#Returns a 200 response.
#If an artist with the supplied artist ID doesn't exist, returns a 404 response
    elif request.method == 'DELETE':
        return deleteArtist(id)







