from flask import Flask, render_template, request
import pymysql
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return "helloworld"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            db="manager"
        )
        mycursor = conn.cursor()
        mycursor.execute('select * from userlist where name=%s', (name,))
        user = mycursor.fetchone()
        if not user:
            return "用户不存在"
        else:
            if user[2] != password:
                return "密码错误"
            else:
                return "登陆成功"


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        now = datetime.datetime.now()
        mysql_datetime = now.strftime('%Y-%m-%d %H:%M:%S')
        user = {
            "name": request.form.get("username"),
            "password": request.form.get("password"),
            "department": request.form.get("department"),
            "email": request.form.get("email"),
            "createtime": mysql_datetime
        }
        conn = pymysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="123456",
            db="manager"
        )
        mycursor = conn.cursor()
        sql = "insert into userlist(name,password,department,email,createtime) values(%(name)s,%(password)s," \
              "%(department)s,%(email)s,%(createtime)s)"
        mycursor.execute(sql, user)
        conn.commit()
        mycursor.close()
        conn.close()
        return "done"


@app.route('/show')
def showusers():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="123456",
        db="manager"
    )
    mycursor = conn.cursor()
    mycursor.execute('select * from userlist')
    data_list = mycursor.fetchall()
    for i in data_list:
        print(i)
    mycursor.close()
    conn.close()

    return render_template('user.html', data_list=data_list)


if __name__ == '__main__':
    app.run()
