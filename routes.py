from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

bunk_data = [
{'subject':'Soft Computing Techniques','bunks':12,'present':29},
{'subject':'Cloud Computing','bunks':9,'present':36},
{'subject':'Middleware Technologies','bunks':14,'present':27},
{'subject':'Mobile Computing','bunks':14,'present':26},
{'subject':'Middleware Technologies Lab','bunks':6,'present':21},
{'subject':'Mobile Computing Lab','bunks':7,'present':23},
{'subject':'Embedded Systems','bunks':10,'present':43},
{'subject':'Green Technology','bunks':12,'present':34}
]

@app.route('/bunkbazaar')
def bunkbazaar():
	return render_template('app.html', bunk_data = bunk_data)

@app.route('/input')
def inputs():
	return render_template('input.html')

if __name__ == '__main__':
	app.run(debug=True)