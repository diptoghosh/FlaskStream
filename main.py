from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        print(request.form)
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()