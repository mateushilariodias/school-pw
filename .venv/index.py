from flask import Flask, render_template, request, redirect, url_for;
import mysql.connector;

app = Flask(__name__);

@app.route('/')
def root():
    return render_template('inicio.html', titulo="Vamos logar?")

@app.route('/login')
def loginRender():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    password_user = request.form['password_user']

    if login_user == '196' and password_user == '@Ma8':
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('inicio', titulo="Usuário ou senha inválido"))
    
@app.route('/inicio')
def inicio():
    return render_template('inicio.html', titulo="Usuário ou senha inválido")

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/cadastro-usuario', methods=['POST'])
def cadastroUsuario():
    login_user = request.form['login']
    password_user = request.form['password_user']
    return render_template('cadastro-cliente')

@app.route('/cadastro-usuario')
def cadastroUser():
    return render_template('cadastro-usuario.html')

# @app.route("/cadastro-usuario/cadastro-cliente")
# def createCliente():
#     return render_template('cadastro-cliente.html')

@app.route('/cadastro-cliente')
def cadastroCliente():
    return render_template('cadastro-cliente.html')

# def conexao_banco():
#     db = mysql.connector.connect(host=, user=, password=, database=)
#     mycursor = db.cursor()
#     query = "INSERT INTO  clientes (usuario, senha) VALUES (%s, %s)"
#     mycursor.execute(query)

app.run();