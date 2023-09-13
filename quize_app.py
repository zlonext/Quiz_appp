# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Завантаження питань з файлу quiz.json
import json

with open("templates/quiz.json", "r", encoding="utf-8") as file:
    data = json.load(file)

questions = data["питання"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'GET':
        return render_template('quiz.html', questions=questions)
    elif request.method == 'POST':
        score = 0
        for i, question in enumerate(questions):
            user_answer = request.form.get(f"question_{i+1}")
            if user_answer is not None and int(user_answer) == question['right']:
                score += 1
        return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
