from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

bunk_data = {'subject':'Soft Computing Techniques','bunks':12,'present':29}

@app.route('/bunkbazaar')
def bunkbazaar():
	return render_template('app.html', bunk_data = bunk_data)

@app.route('/input')
def inputs():
	return render_template('input.html')
if __name__ == '__main__':
	app.run(debug=True)