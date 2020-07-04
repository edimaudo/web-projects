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
    if request.method == 'GET':
        return get_artist(id)
    elif request.method == 'PUT':
    	artist_name = request.args.get('artist_name', '')
    	date_of_birth = request.args.get('date_of_birth', '')
    	biography = request.args.get('biography', '')
    	is_currently_employed = request.args.get('is_currently_employed','')
    	return updateArtist(id, artist_name, date_of_birth, biography, is_currently_employed)
    elif request.method == 'DELETE':
    	return deleteArtist(id)

#==============
#Series html routing
#==============
@app.route('/series')
def showSeries():
	artists = session.query(Series).all()
	return render_template('series.html', series=series)

@app.route('/series/new/', methods=['GET', 'POST'])
def newSeries():
    if request.method == 'POST':
        newArtist = Series(series_name=request.form['series_name'],
                       description=request.form['description'])
        session.add(newSeries)
        session.commit()
        return redirect(url_for('showSeries'))
    else:
        return render_template('newSeries.html')

#==============
#Series api functions
#==============
def get_series():
    series = session.query(series).all()
    return jsonify(series=[a.serialize for a in series])	

def getAseries(series_id):
	series = session.query(series).filter_by(id=series_id).one()
	#add check if id does not exist
	return jsonify(series=series.serialize)

def makeANewseries(series_name, description):
	addedseries = series(series_name = series_name, description = description)
	session.add(addedseries)
	session.commit()
	return jsonify(series=addedseries.serialize)

def updateSeries(id, series_name, description):
    updatedseries = session.query(Series).filter_by(id=id).one()
    if not series_name:
        updatedseries.series_name = series_name
    if not description:
        updatedseries.description = description
    session.add(updatedseries)
    session.commit()
    return 'Updated an series with id %s' % id

def deleteSeries(id):
    seriesToDelete = session.query(series).filter_by(id=id).one()
    session.delete(seriesToDelete)
    session.commit()
    return 'Removed series with id %s' % id

#==============
#Series API routing
#==============
#/api/series
@app.route('/seriesApi', methods=['GET', 'POST'])
def seriesFunction():
    if request.method == 'GET':
        return get_series()
    elif request.method == 'POST':
        series_name = request.args.get('series_name', '')
        description = request.args.get('description', '')
        return makeANewSeries(series_name, description)

#/api/series/:seriesId
@app.route('/seriesApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def seriesFunctionId(id):
    if request.method == 'GET':
        return getAseries(id)
    elif request.method == 'PUT':
    	series_name = request.args.get('series_name', '')
    	description = request.args.get('description', '')
    	return updateSeries(id, series_name, description)
    elif request.method == 'DELETE':
        return deleteSeries(id)

#==============
#Issues api functions
#==============
def get_issues():
    issue = session.query(issue).all()
    return jsonify(issue=[a.serialize for a in issue])    

def get_issue(issue_id):
    issue = session.query(issue).filter_by(id=issue_id).one()
    #add check if id does not exist
    return jsonify(issue=issue.serialize)

def makeANewissue(issue_name, issue_number, publication_date, series_id):
    addedissue = issue(issue_name = issue_name, issue_number = issue_number, publication_date = publication_date, 
    	series_id = series_id)
    session.add(addedissue)
    session.commit()
    return jsonify(issue=addedissue.serialize)

def updateIssue(id, issue_name, issue_number, publication_date):
    updatedissue = session.query(issue).filter_by(id=id).one()
    if not issue_name:
        updatedissue.issue_name = issue_name
    if not issue_number:
        updatedissue.issue_number = issue_number
    if not publication_date:
        updatedissue.publication_date = publication_date
    session.add(updatedissue)
    session.commit()
    return 'Updated an issue with id %s' % id

def deleteIssue(id):
    issueToDelete = session.query(issue).filter_by(id=id).one()
    session.delete(issueToDelete)
    session.commit()
    return 'Removed issue with id %s' % id


#==============
#Issues API routing
#==============

#/api/series/:seriesId/issues
@app.route('/seriesApi/<int:id/issues', methods=['GET', 'POST'])
def seriesFunction(id):
    if request.method == 'GET':
        return get_issues()
    elif request.method == 'POST':
        issue_name = request.args.get('issue_name', '')
        issue_number = request.args.get('issue_number', '')
        publication_date = request.args.get('publication_date','')
        series_id = id
        return makeANewIssue(issue_name, issue_number, publication_date, series_id)


@app.route('/seriesApi/<int:series_id>/issues/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def seriesFunctionId(id):
    if request.method == 'GET':
        return get_issue(id)
    elif request.method == 'PUT':
    	issue_name = request.args.get('issue_name', '')
    	issue_number = request.args.get('issue_number', '')
    	publication_date = request.args.get('publication_date','')
    	return updateIssue(id, issue_name, issue_number, publication_date)
    elif request.method == 'DELETE':
        return deleteIssue(id)

