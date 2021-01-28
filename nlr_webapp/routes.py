from nlr_webapp import app
from nlr_webapp.forms import QueryForm

@app.route("/", methods=['GET', 'POST'])
def home():
    form_result = QueryForm()

    if form.validate_on_submit():
        print("good")

    return "Natural Language Recommendations"
