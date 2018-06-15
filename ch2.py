from flask import Flask,render_template

app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
	user = {'username' : 'Nann Khaing'}
	
	posts = [{
		'author' : {'username': 'Khaing Khaing'},
		'body' : ' Beautiful day in Portland!'
	},
	{
		'author' : {'username': 'Nann La Min Khaing'},
		'body' : 'The Avengers movie was so cool!'
	}
	]
	return render_template('index.html', title ='Home', user = user, posts = posts)
if __name__ == '__main__':
	app.run(debug=True)