from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    # Start new game
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ''
    
    if request.method == 'POST':
        guess = request.form.get('guess')
        if guess and guess.isdigit():
            guess = int(guess)
            session['attempts'] += 1
            if guess < session['number']:
                message = 'Too low! 📉'
            elif guess > session['number']:
                message = 'Too high! 📈'
            else:
                message = f'Correct! 🎉 You guessed it in {session["attempts"]} attempts.'
                session.pop('number')
                session.pop('attempts')

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
