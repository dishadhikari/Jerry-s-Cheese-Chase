from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-game')
def run_game():
    subprocess.Popen(['python', 'main.py'], cwd=os.path.dirname(os.path.abspath(__file__)))
    return "Game launched!"

if __name__ == '__main__':
    app.run(debug=True)
