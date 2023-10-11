from flask import Flask, render_template, request

app = Flask(__name__);

@app.route('/')
def inicio():
    return render_template('inicio.html', titulo="Vamos logar?")

@app.route('/login')
def loginRender():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    password_user = request.form['password_user']

    if login_user == '196' and password_user == '@Ma8':
        return render_template('homepage.html')
    else:
        return render_template('inicio.html', titulo="Usuário ou senha inválido")
    
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

app.run();