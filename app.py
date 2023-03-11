from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('blog.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)


@app.route('/getregister')
def get_register():
    print(request.args)
    return "Done"


@app.route('/userlist')
def showuser():
    users = ["Tom", "Jerry", "Brain", "Sam"]
    return render_template('users.html', title="HAHA", data_list=users)


if __name__ == '__main__':
    app.run()
