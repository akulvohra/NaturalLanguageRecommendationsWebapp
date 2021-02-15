from flask import url_for, redirect, render_template, request
#from nlr_webapp.recommender import Infer

from nlr_webapp import app
from nlr_webapp.forms import QueryForm

@app.route("/", methods=['GET', 'POST'])
def home():
    form = QueryForm()
    if request.method == 'GET':
        return render_template('home.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            print("form validated")
            #title, abstract, link = Infer(form.query.data, form.top_k.data)
            #put flash for generating here
            title, abstract, link = ["T1", "T2", "T3"], ["lipsum 1", "lipsum 1", "lipsum 1"], ["https://link.com", "https://link.com", "https://link.com"]
            results = zip(title, abstract, link)
            print("inference generated")
            return render_template('home.html', form=form, results=results)
        else:
            return render_template('home.html', form=form)
