from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

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
    

@app.route('/main')
def main():
	return "Hello, Main!"