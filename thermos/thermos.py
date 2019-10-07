from flask import Flask , render_template, url_for, request, redirect, flash
from datetime import datetime

from forms import BookmarkForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'

bookmarks = []

def store_bookmark(url,description):
	bookmarks.append(dict(
		url = url,
		user = "Miguel",
		description = description,
		date = datetime.utcnow
	))

def new_bookmarks(num):
    return sorted(bookmarks,reverse=True)[:num]

class User:
	def __init__(self,firstname,lastname):
		self.firstname = firstname
		self.lastname = lastname

	def initials(self):
		return "{}. {}.".format(self.firstname[0],self.lastname[0])


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', new_bookmarks = new_bookmarks(5) )

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        url = form.url.data
        description = form.description.data
        store_bookmark(url, description)
        flash("Stored '{}'".format(description))
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404 ## tuples returning html page, and status error.

@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

if __name__ == '__main__':
	app.run(debug=True)


