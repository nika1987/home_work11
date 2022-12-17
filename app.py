import utils
from flask import Flask, render_template
from constants import DATA_FILE

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
    data = utils.load_candidates_from_json(DATA_FILE)
    return render_template("list.html", data=data)


@app.route('/candidate/<int:uid>')
def get_candidates(uid):
    candidate = utils.get_candidate(uid)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def search_by_name(candidate_name):
    candidate_list = utils.get_candidates_by_name(candidate_name)
    score_candidate = len(candidate_list)
    return render_template("search.html", candidate_list=candidate_list, score=score_candidate)


@app.route('/skill/<skill_name>')
def search_by_skills(skill_name):
    candidate_list = utils.get_candidates_by_skill(skill_name)
    score_candidate = len(candidate_list)
    return render_template("search.html", candidate_list=candidate_list, score=score_candidate,skill=skill_name)


app.run()
