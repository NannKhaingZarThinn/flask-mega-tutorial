from flask import Flask, abort, request

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Friends to all!'

@app.route('/hello/<name>')
@app.route('/hello/')
def hello(name=None):
	if name is None:
		# If no
		# from the
		if name:
			return 'Hello, %s' % name
	else:
		# No one was
		abort(404)
	
if __name__ == '__main__':
	app.run(debug=True)