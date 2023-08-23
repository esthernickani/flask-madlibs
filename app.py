from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__, template_folder = "templates")

if __name__ == "main":
    app.debug = True
    app.run()

app.config['SECRET_KEY'] = "hellothere"

toolbar = DebugToolbarExtension(app)

story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

@app.route('/')
def show_form():
    """This shows the html form for the user to choose what parts of speech they want for their story"""
    prompts = story.prompts
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def show_story():
    """This returns the story and shows it on the webpage"""
    
    place = request.args["place"]
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    answer = {
        "place":place, 
        "noun":noun, 
        "verb":verb, 
        "adjective":adjective, 
        "plural_noun":plural_noun
    }

    user_story = story.generate(answer)

    return render_template("story.html", user_story=user_story)






