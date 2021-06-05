from flask import Flask, render_template, request
from flask.helpers import url_for
from flask.wrappers import Response
from werkzeug.utils import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

class contacts(database.Model):

    __tabelname__ = 'contacts'
    _id = database.Column("id", database.Integer, primary_key = True)
    name = database.Column("name", database.String(255))
    email = database.Column("email", database.String(255))
    subject = database.Column("subject", database.String(1000))
    message = database.Column("message", database.String(5000))

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message


@app.route('/',  methods = ['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        contact = contacts(name = name, email = email, 
        subject = subject, message= message)
        database.session.add(contact)
        database.session.commit()

        return render_template('index.html')

    return render_template('index.html')

if __name__ == '__main__':
    database.create_all()
    app.run(debug = True)
