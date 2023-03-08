from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        name = request.form.get('name')
        password = request.form.get('password')
        print(name, password)


# @app.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "GET":
#         return render_template('register.html')
#     else:
#         name = request.form.get('username')
#         password = request.form.get('password')
#         gender = request.form.get('gender')
#         language = request.form.getlist('language')
#         city = request.form.get('city')
#         message = request.form.get('message')
#         print(name, password, gender, language, city, message)
#         return "Done"
#

@app.route('/getregister')
def get_register():
    print(request.args)
    return "Done"


if __name__ == '__main__':
    app.run()
