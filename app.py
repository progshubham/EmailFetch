from flask import Flask, Response, send_from_directory, render_template, request, flash, session, abort, json
from flask import url_for, redirect
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
import os.path
import jinja2
import re
import os
import urllib


app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
app.secret_key = os.urandom(24)

jinja_environment = jinja2.Environment(autoescape=True,
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))



@app.route("/")
# @app.cache.cached(timeout=300)  # cache this view for 5 minutes
def index():

	return render_template('index.html').encode( "utf-8" )

@app.route("/result",methods=['POST'])
# @app.cache.cached(timeout=300)  # cache this view for 5 minutes
def result():
	url = str(request.form['url'].encode('utf-8'))
	f = urllib.urlopen(url)
	s = f.read()
	re.findall(r"\+\d{2}\s?0?\d{10}",s)
	s = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
	s = json.dumps(s)
	f = open('data.csv','w')
	f.write(s)
	f.close()
	# return str(s)
	return render_template('result.html', s = s).encode( "utf-8" )


if __name__ == "__main__":
	app.run(host='0.0.0.0',threaded=True,debug=True)