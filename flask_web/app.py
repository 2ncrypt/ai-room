from flask import Flask, render_template, request, redirect, flash
from data import Articles
import pymysql
from passlib.hash import sha256_crypt


app = Flask(__name__)
app.debug = True
db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='ekthdlek12',
    db='busan'
)


@app.route('/main', methods=['GET'])
def index():
  # return "Hello World"
  return render_template("main.html", data="KIM")


@app.route('/abt')
def about():
  return render_template("about.html", hello="Gary Kim")


@app.route('/art')
def articles():
  cursor = db.cursor()
  sql = 'SELECT * FROM topic;'
  cursor.execute(sql)
  topics = cursor.fetchall()
  # print(topics)
  # articles = Articles()
  # print(articles[0]['title'])
  return render_template("articles.html", article=topics)


@app.route('/article/<int:id>')
def article(id):
  cursor = db.cursor()
  sql = 'SELECT * FROM topic WHERE id={}'.format(id)
  cursor.execute(sql)
  topic = cursor.fetchone()  # fetchone과 fetchall의 차이
  # articles = Articles()
  # article = articles[id-1]
  return render_template("article.html", article=topic)


@app.route('/art_add', methods=["GET", "POST"])
def art_add():
  cursor = db.cursor()
  if request.method == "POST":
    title = request.form['title']
    author = request.form['author']
    desc = request.form['description']

    sql = 'INSERT INTO `topic` (`title`, `author`, `body`) VALUES (%s, %s, %s);'
    input_data = [title, author, desc]
    cursor.execute(sql, input_data)
    db.commit()
    # db.close()
    return redirect('/art')
  else:
    return render_template("art_add.html")


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
  cousour = db.cursor()
  # sql = 'DELETE FROM `topic` WHERE id = %s;'
  # id = [id]
  # cousour.execute(sql, id)
  sql = 'DELETE FROM `topic` WHERE id = {};'.format(id)
  cousour.execute(sql)
  db.commit()
  return redirect('/art')


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    cursor = db.cursor()
    if request.method == "POST":
      title = request.form['title']
      author = request.form['author']
      desc = request.form['description']

      sql = 'UPDATE `busan`.`topic` SET title = %s , author = %s ,body = %s WHERE id ={} ;'.format(id)
      update_data = [title, author, desc ]
      cursor.execute(sql, update_data)
      db.commit()
      return redirect(f'/article/{id}')

    else:
        sql = "SELECT * FROM topic WHERE id = {}".format(id)
        cursor.execute(sql)
        topic = cursor.fetchone()
        # print(topic, '\n')

        print(topic[1])
        return render_template("art_edit.html", article=topic)

@app.route('/assignment', methods=["GET", "POST"])
def assinment():  
  cursor = db.cursor()
  if request.method == "POST":
    userid = request.form['userid']
    userpwd = sha256_crypt.encrypt(request.form['password'])
    number = request.form['number']
    email = request.form['email']

    # pwcrypt = sha256_crypt.verify("password",password)
    # if pwcrypt == TRUE :
    sql = 'INSERT INTO `assignment` (`userid`, `userpwd`, `number`, `email`) VALUES (%s, %s, %s,%s);'
    asg_data = [userid, userpwd, number, email]
    cursor.execute(sql, asg_data)
    db.commit()
    # db.close()
    # flash("Assignment Success")
    return redirect('/main')
  else:
    return render_template("assignment.html")

@app.route('/login',methods=["GET","POST"])
def login():
  cursor = db.cursor()
  if request.method =="POST":
    userid_ = request.form['userid']
    userpw_ = request.form['userpw']
    print(userid_)
    print(userpw_)
    sql = 'SELECT userpwd FROM assignment WHERE email = %s;'
    input_data = [userid_]
    cursor.execute(sql, input_data)
    userpw = cursor.fetchone()
    if sha256_crypt.verify(userpw_,userpw[0]):
      return "TEST"
  else:
    return userpw[0]

if __name__ == '__main__':
  app.run()
