from flask import Flask, render_template, redirect, request, flash, url_for
from forms import ContactForm

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

app.secret_key = '654c6da8f3b0fd8fe819669daf07996738d21a53c02c731b0aee6373'

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

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
	if request.method == 'POST':
		name = request.form['name']
		email = request.form['email']
		subject = request.form['subject']
		message = request.form['message']
		print name
		return render_template('contactsuccess.html', name=name, email=email, subject=subject, message=message)
	elif request.method == 'GET':
		return render_template('contact.html')

#@app.route('/contactsucess')
#def contact_success():
#	return render_template('')
	

if __name__ == '__main__':
	app.run(debug=True)