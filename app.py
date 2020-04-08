from flask import Flask, render_template, url_for

app = Flask(__name__)

roster = [
{
	'name':'Gehan Jayatilaka', 
	'info':'4th Year B.S., Mechanical Engineering'
},
{
	'name':'Nicolas Renteria',
	'info':'4th Year B.S., Mechanical Engineering'
}
]

@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html')


@app.route('/sub')
def sub():
	return render_template('sub.html', roster=roster)


if __name__ == "__main__":
	app.run(debug=True)