from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__, template_folder = "templates")

if __name__ == "main":
    app.debug = True
    app.run()

app.config['SECRET_KEY'] = "hellothere"

toolbar = DebugToolbarExtension(app)


@app.route('/')
def show_form():
    """This shows the html form for the user to choose what parts of speech they want for their story"""
    return render_template("form.html")

@app.route('/story')
def show_story():
    """This returns the story and shows it on the webpage"""
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    return render_template("story.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)






