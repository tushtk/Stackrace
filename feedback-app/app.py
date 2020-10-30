
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_mail

app = Flask(__name__)

ENV = 'prod' 

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tada@localhost/stackrace_01'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hazbpuuybzwgoq:7cb05011c7125d9121e913ce0118a34e7e339584597601b04f542a3ca60b8618@ec2-3-223-21-106.compute-1.amazonaws.com:5432/dcqvbp1rb9ql5s'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), unique=True)
    city = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, user, city, rating, comments):
        self.user = user
        self.city = city
        self.rating = rating
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        user = request.form['user']
        city = request.form['city']
        rating = request.form['rating']
        comments = request.form['comments']
        print(user,city,rating,comments)
        if user == '' or city =='':
            return render_template('index.html',message ="Please enter your name/city")
        
        if db.session.query(feedback).filter(feedback.user==user).count() == 0: 
            data  = feedback(user,city,rating,comments)
            db.session.add(data)
            db.session.commit()
            send_mail(user,city,rating,comments)
            return render_template('success.html')
        
        return render_template('index.html',message ="Already submitted previously")
        

if __name__ == '__main__':
    
    app.run()

