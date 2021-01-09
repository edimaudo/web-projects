from app import app
from flask import render_template, flash, redirect, url_for, request, make_response
from app import db
from app.models import Minion, Idea, Meeting, Work

#helper functions
def isMillionDollarIdea(weeklyRevenue, numWeeks):
    totalMoney = numWeeks * weeklyRevenue
    if totalMoney < 1000000:
        return True
    return False

#==========
#error handlers
#==========
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

#==========
#home
#==========
@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")

#==========
#minions
#==========
#to get an array of all minions.
@app.route('/minions')
def minions():
    all_data = Minion.query.all()
    return render_template("minion.html", minions = all_data)

#to create a new minion and save it to the database.
@app.route("/minions/add", methods=["GET", "POST"])
def minions_add():
    if request.method == "POST":
        name = request.form['name']
        title = request.form['title']
        salary = request.form['salary']
        my_data = Minion(name, title, salary)
        db.session.add(my_data)
        db.session.commit()
        flash("Minion added successfully")
        return redirect(url_for('minions'))
    return render_template('minion_add.html')

#to get a single minion by id.
@app.route('/minions/view/<int:minion_id>')
def minions_view(minion_id):
	my_data = Minion.query.get(minion_id)
	return render_template("minion_view.html", minion = my_data)

#to update a single minion by id.
@app.route('/minions/update/<int:minion_id>',methods = ['GET', 'POST'])
def minion_update(minion_id):
	if request.method == "POST":
		my_data = Minion.query.get(minion_id)
		my_data.name = request.form['name']
		my_data.title = request.form['title']
		my_data.salary = request.form['salary']
		db.session.commit()
		flash("Minion updated succesfully")
		return redirect(url_for("minions"))
	else:
		minion = Minion.query.get(minion_id)
		return render_template("minion_update.html", minion = minion)

#to delete a single minion by id.
@app.route("/minions/delete/<int:minion_id>")
def minion_delete(minion_id):
	my_data = Minion.query.get(minion_id)
	db.session.delete(my_data)
	db.session.commit()
	flash("Minion deleted succesfully")
	return redirect(url_for("minions"))

#==========
#ideas
#==========
#to get an array of all ideas.
@app.route('/ideas')
def ideas():
    all_data = Idea.query.all()
    return render_template("idea.html",  ideas = all_data)

#to create a new idea and save it to the database.
@app.route("/ideas/add", methods=["GET", "POST"])
def ideas_add():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        numWeeks = request.form['numWeeks']
        weeklyRevenue = request.form['weeklyRevenue']
        my_data = Idea(name, title, salary)
        db.session.add(my_data)
        db.session.commit()
        flash("idea added successfully")
        return redirect(url_for('ideas'))
    return render_template('idea_add.html')

#to get a single idea by id.
@app.route('/ideas/view/<int:idea_id>')
def ideas_view(idea_id):
	my_data = Idea.query.get(idea_id)
	return render_template("idea_view.html", idea = my_data)

#to update a single idea by id.
@app.route('/ideas/update/<int:idea_id>',methods = ['GET', 'POST'])
def idea_update(idea_id):
    if request.method == "POST":
        my_data = Idea.query.get(idea_id)
        my_data.name = request.form['name']
        my_data.description = request.form['description']
        my_data.numWeeks = request.form['numWeeks']
        my_data.weeklyRevenue = request.form['weeklyRevenue']
        db.session.commit()
        flash("idea updated succesfully")
        return redirect(url_for("ideas"))
    else:
        idea = Idea.query.get(idea_id)
        return render_template("idea_update.html", idea = idea)
		
		

#to delete a single idea by id.
@app.route("/ideas/delete/<int:idea_id>")
def idea_delete(idea_id):
	my_data = Idea.query.get(idea_id)
	db.session.delete(my_data)
	db.session.commit()
	flash("idea deleted succesfully")
	return redirect(url_for("ideas"))


#==========
#meetings
#==========
#to get an array of all meetings.
@app.route("/meetings")
def meetings():
    all_data = Meeting.query.all()
    return render_template("meetings.html", meetings = all_data)

#to create a new meeting and save it to the database.
@app.route("/meetings/add", methods=["GET", "POST"])
def meetings_add():
    if request.method == "POST":
        day = request.form['day']
        date = request.form['date']
        note = request.form['note']
        my_data = Meeting(date, day, note)
        db.session.add(my_data)
        db.session.commit()
        flash("Meeting added successfully")
        return redirect(url_for('meetings'))
    return render_template('meetings_add.html')

#to delete all meetings from the database.
@app.route("/meetings/delete")
def meetings_delete():
	my_data = Meeting.query.all()
	db.session.delete(my_data)
	db.session.commit()
	flash("Meetings deleted succesfully")
	return redirect(url_for("meetings"))

#==========
#works
#==========

@app.route("/work")
def work():
    all_data = Work.query.all()
    return render_template("work.html", work = all_data)

#to get an array of all work for the specified minon.
@app.route('/minions/<int:minion_id>/work')
def work_view(minion_id):
	my_data = Work.query.get(minion_id)
	return render_template("work_view.html", idea = my_data)

#to create a new work object and save it to the database.
@app.route("/minions/<int:minion_id>/work/add", methods=["GET", "POST"])
def work_add():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        hours = request.form['hours']
        minion_id = request.form['minion_id']
        my_data = Work(title, description, hours, minion_id)
        db.session.add(my_data)
        db.session.commit()
        flash("Work added successfully")
        return redirect(url_for('work'))
    return render_template('work_add.html')

#to update a single work by id.
@app.route('/minions/<int:minion_id>/work/<int:work_id>',methods = ['GET', 'POST'])
def work_update(minion_id, work_id):
	if request.method == "POST":
		my_data = Work.query.filter(minion_id == minion_id).filter(work_id == work_id).all()
		my_data.title = request.form['title']
		my_data.description = request.form['description']
		my_data.hours = request.form['hours']
		db.session.commit()
		flash("Work updated succesfully")
		return redirect(url_for("work"))
	else:
		idea = Idea.query.get(idea_id)
		return render_template("work_update.html", idea = idea)

# to delete a single work by id.
@app.route("/minions/<int:minion_id>/work/<int:work_id>/delete")
def work_delete(minion_id, work_id):
	my_data = Work.query.filter(minion_id == minion_id).filter(work_id == work_id).all()
	db.session.delete(my_data)
	db.session.commit()
	flash("Work deleted succesfully")
	return redirect(url_for("work"))

















