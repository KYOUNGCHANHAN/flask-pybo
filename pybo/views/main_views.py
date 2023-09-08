from flask import Blueprint, url_for # render_template
from werkzeug.utils import redirect

# from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/') # url 프리픽스: 함수호출 localhost:5000/


@bp.route('/hello') #url 프리픽스: 함수호출 localhost:5000/
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# @bp.route('/')
# def index():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('question/question_list.html', question_list=question_list)
#     return 'Pybo index'

# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get_or_404(question_id)
#     return render_template('question/question_detail.html', question=question)
