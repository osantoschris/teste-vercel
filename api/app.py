from flask import Flask, render_template, url_for, redirect, request, session, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        username = request.form['username'] 
        password = request.form['password']

        if username == 'christian.oliveira' and password == 'christian':
            session['user_id'] = 1
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html')
    else:
        flash('É necessário realizar o login antes de acessar o dashboard.', 'warning')
        return redirect(url_for('login'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)