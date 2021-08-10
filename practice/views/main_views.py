from flask import Blueprint, render_template
from practice.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    question_list = Question.query.order_by(Question.create_date.desc())
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/hello')
def hello_world():
    return 'Hello World'