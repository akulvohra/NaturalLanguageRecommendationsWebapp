from flask import url_for, redirect, render_template

from nlr_webapp import app
from nlr_webapp.forms import QueryForm

@app.route("/", methods=['GET', 'POST'])
def home():
    form = QueryForm()

    if form.validate_on_submit():
        print("good")

    return render_template('home.html', form=form)
