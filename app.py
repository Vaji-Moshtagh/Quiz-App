from flask import Flask, request, render_template, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed to keep session secure

@app.route('/')
def home():
    # Reset score and load questions
    session['score'] = 0
    session['question_index'] = 0
    with open('questions.json', 'r') as file:
        session['questions'] = json.load(file)
    return redirect(url_for('quiz'))

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        user_answer = request.form['answer']
        correct_answer = session['questions'][session['question_index']]['answer']
        if user_answer == correct_answer:
            session['score'] += 1
        session['question_index'] += 1

    if session['question_index'] == len(session['questions']):
        return redirect(url_for('results'))

    question = session['questions'][session['question_index']]
    return render_template('quiz.html', question=question)

@app.route('/results')
def results():
    return render_template('results.html', score=session['score'], total=len(session['questions']))

if __name__ == '__main__':
    app.run(debug=True)
