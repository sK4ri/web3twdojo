from flask import Flask, render_template, redirect, request
from data_manager import *
app = Flask(__name__)


@app.route('/')
def see_main_page():
    return render_template('index.html')


@app.route('/applicants')
def see_applicants():
    applicants = get_applicants()
    return render_template('applicants.html', applicants=applicants)

#
# @app.route('/applicants/<int:applicant_id>')
# def see_applicants(applicants_id):
#     question = get_question_by_id(question_id)
#     answers = get_answers_by_q_id(question_id)
#     if not request.args.get('inc'):
#         pass
#     return render_template('question.html', question=question, answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
