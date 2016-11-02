from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setup_database import Base, Categories, Items

app = Flask(__name__)

engine = create_engine('sqlite:///catelogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/testpage')
def TestPage():
  return render_template('testpage.html')

@app.route('/home')
def HomePage():
  categories = session.query(Categories).order_by(Categories.id)
  items = session.query(Items).order_by(Items.id)
  return render_template('homePage.html', categories = categories, items = items)

"""
-- uncomment the following  route if you would like to add more categories to the list --

@app.route('/createcategory', methods=['GET', 'POST'])
def CreateCategory():
    if request.method == 'POST':
        newCategory = Categories(category = request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('createCategory.html')


    categories = session.query(Categories).order_by(Categories.id)
    items = session.query(Items).order_by(Items.id)
"""
@app.route('/createitem', methods = ['GET', 'POST'])
def AddItem():
    categories = session.query(Categories).order_by(Categories.id)
    if request.method == 'POST':
        newItem = Items(title = request.form['title'],
                        description = reqest.form['description'],
                        category_id = request.form['category_id'])
        session.add(newItem)
        session.commit()
        return redirect(url_for('HomePage'))
    return render_template('createItems.html', categories = categories)


if __name__ == '__main__':
    app.secret_key = "Secret_Key"
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)
