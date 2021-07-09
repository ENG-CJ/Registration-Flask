from flask import Flask,redirect,request,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///students.db'

db=SQLAlchemy(app)

# modal
class Student(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    FirstName=db.Column(db.String(100), nullable=False)
    LastName=db.Column(db.String(90), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    mobile=db.Column(db.String(100),nullable=False)



@app.route('/',methods=['POST','GET'])
def home():
    return 'Home Page'

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['mail']
        mobile=request.form['mobile']
        content=Student(FirstName=fname,LastName=lname,email=email,mobile=mobile)
        db.session.add(content)
        db.session.commit()
        return redirect(url_for('user'))
    return render_template('index.html')
    
    
@app.route('/user',methods=['POST','GET'])
def user():
    users=Student.query.all()
    return render_template('user.html',users=users)

@app.route('/students/delete/<int:id>')
def delete(id):
    delete_=Student.query.get_or_404(id)
    db.session.delete(delete_)
    db.session.commit()
    return redirect(url_for('user'))
if __name__=="__main__":
    app.run(debug=True)