from flask import render_template,Flask,redirect, flash, url_for
app = Flask(__name__)
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.username.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
@app.route('/index')
def index():
	user = {'username' : 'Minguel'}
	return render_template('index.html', title = 'Home', user = users)
	
if __name__ == '__main__':
	app.run(debug=True)