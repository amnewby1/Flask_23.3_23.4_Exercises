<<<<<<< HEAD
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from surveys import satisfaction_survey
app = Flask(__name__)

app.config['SECRET_KEY'] = "amanda1"
debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def make_homepage():
    title = satisfaction_survey.title
    instructions = satisfaction_survey.instructions
    return render_template('home.html', title = title, instructions=instructions)
=======
from flask import Flask, render_template, session, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Amanda1'

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False

response_list = "answers"

@app.route('/')
def start_page():
    title = survey.title
    instructions = survey.instructions
    return render_template('/start_page.html', title=title, instructions=instructions)


@app.route('/start_survey', methods=['POST'])
def start_survey():
    session[response_list] = []
    return render_template('/questions/0')


@app.route('/questions/<int:question_number>')
def handle_questions(question_number):
    answers = session.get(response_list)
    
    if (answers is None):
        return redirect('/')
    
    if (len(answers) == len(survey.questions)):
        return redirect('/finished')
    
    if len(answers) != question_number:
        flash(f"You can't access {question_number} yet!")
        return redirect(f'/questions/{len(answers)}')
    
    question = survey.questions[question_number]
    
    return render_template('questions.html', question = 
    question, question_number=question_number)


@app.route('/answer', methods=['POST'])
def handle_answer():
    choice = request.form['answer']

    answers = session[response_list]
    answers.append(choice)
    session[response_list]=answers

    if (len(answers) == len(survey.questions)):
        return redirect ('/finished')
    
    else:
        return redirect(f"/questions/{len(answers)}")

@app.route('/finished')
def finished_survey():  
    return render_template('finished.html')
  
>>>>>>> 57eeedc (re-written code)
