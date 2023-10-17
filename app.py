from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy database object
db = SQLAlchemy(app)

# Define your database model (TestModel in this case)
class TestModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255))
    comment = db.Column(db.String(255))

# Define a function to create the tables
def create_tables():
    with app.app_context():
        db.create_all()

# Create a database if it doesn't exist
create_tables()

@app.route("/")
def home():
    return render_template("startpage.html")

@app.route("/data/create", methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        id = request.form['id']
        url = request.form['url']
        comment = request.form['comment']

        test_list = TestModel(id=id, url=url, comment=comment)
        db.session.add(test_list)
        db.session.commit()

        return redirect('/data')

@app.route("/data")
def RetrieveDataList():
    testlists = TestModel.query.all()
    return render_template("datalist.html", testlists=testlists)

@app.route("/data/<int:id>")
def RetrieveOneRecord(id):
    list_element = TestModel.query.filter_by(id=id).first()
    if list_element:
        return render_template('data.html', list_element=list_element)
    return f"Record with ID: {id} does not exist"

if __name__ == "__main__":
    app.run()
