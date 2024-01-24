from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

#
app.config['SQLALCHEMU_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    data_created = db.Column(d)    

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug= True)
    
    