from app import app
from flask import render_template

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    #user = {'username': 'Miguel'}
    #return render_template('index.html', title='Home', user=user)

 # this style of code is bad because you would have to change your template everything your code changes
 # a better option is to use a template
 #    user = {'username': 'Miguel'}
 #    return '''
 #    <html>
 #    <head>
 #        <title>Home Page - Microblog</title>
 #    </head>
 #    <body>
 #        <h1>Hello, ''' + user['username'] + '''!</h1>
 #    </body>
	# </html>'''

 @app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)   

@app.route('/main')
def main():
	return "Hello, Main!"