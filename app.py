from flask import Flask, render_template, request, redirect, url_for
from database import init_db, insert_event

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_scorecard():
    data = request.form
    insert_event(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
