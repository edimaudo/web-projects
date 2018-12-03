from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy #orm
import os

#added db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "ideaBox.db"))


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Idea(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String(140), unique=False, nullable=False)

    def __repr__(self):
    	return "<Idea {}>".format(self.title)



@app.route("/", methods=["GET", "POST"])
def index():
    ideas = None
    if request.form:
        try:
            idea = Idea(title=request.form.get("title"))
            description = Idea(description = request.form.get("description"))
            db.session.add(idea)
            db.session.add(description)
            db.session.commit()
        except Exception as e:
            print("Failed to add idea")
            print(e)
    ideas = Idea.query.all()
    return render_template("index.html", ideas=ideas)

@app.route("/update", methods=["POST"])
def update():
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        newdescription = request.form.get("newdescription")
        idea = Idea.query.filter_by(title=oldtitle).first()
        idea.title = newtitle
        idea.description = newdescription
        db.session.commit()
    except Exception as e:
        print("Couldn't update idea")
        print(e)
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    title = request.form.get("title")
    idea = Idea.query.filter_by(title=title).first()
    db.session.delete(idea)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)