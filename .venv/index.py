from flask import Flask, render_template, request, redirect, url_for;
import mysql.connector;

app = Flask(__name__);

# renderiza a página inicial mostrando para usuário a primeira página
@app.route('/')
def root():
    return render_template('inicio.html', titulo="Vamos logar?")

# na minha página mostra o formulário login e senha
@app.route('/login')
def loginRender():
    return render_template('login.html')

# aqui captura os valores que vem por formulario e renderiza a página 
@app.route('/login', methods=['POST'])
def login():
    login_user = request.form['login']
    password_user = request.form['senha']

    if login_user == 'admin' and password_user == '123':
        return redirect(url_for('homepage'))
    else:
        return redirect(url_for('inicio', titulo="Usuário ou senha inválido"))
# como já tem uma pagina com rota de inicio não tem necessidade de colocar inicio após a barra
@app.route('/')
def inicio():
    return render_template('inicio.html', titulo="Usuário ou senha inválido")

# renderiza para página home Page
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
# ao clicar no link na home page renderiza para página cadastro de usuário

@app.route('/cadastro-usuario')
def cadastroUser():
    return render_template('cadastro-usuario.html')

@app.route('/cadastro-cliente', methods=['POST'])
def cadastroUsuario():
    login_user = request.form['login']
    password_user = request.form['senha']
    return render_template('cadastro-cliente.html')
    #return redirect(url_for('cadastro-cliente'))

@app.route('/cadastro-cliente')
def cadastroCliente():
    return render_template('cadastro-cliente.html')

# @app.route("/cadastro-usuario/cadastro-cliente")
# def createCliente():
#     return render_template('cadastro-cliente.html')

@app.route('/cadastro-cliente/insert', methods=['POST'])
def cadastrarCliente():
    nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['endereco']
    bairro = request.form['bairro']
    cep = request.form['cep']
    cidade = request.form['cidade']
    return render_template('homepage.html')

# def conexao_banco():
#     db = mysql.connector.connect(host=, user=, password=, database=)
#     mycursor = db.cursor()
#     query = "INSERT INTO  clientes (usuario, senha) VALUES (%s, %s)"
#     mycursor.execute(query)

@app.route('/cadastro_usuario', methods=['POST'])
def inserir_usuario():
    login = request.form['login']
    senha = request.form['senha']
    
    db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
    mycursor = db.cursor()
    
    query = 'INSERT INTO mateus_TB_user (usuario, senha) VALUES (%s,%s)'
    values = (login, senha)
    
    mycursor.execute(query, values)
    
    db.commit()
    return render_template('cadastro-cliente.html')

@app.route('/cadastro_cliente', methods=['POST'])
def inserir_cliente():
    nome = request.form['nome']
    if 'nome' in request.form:
        nome = request.form['nome']
    cpf = request.form['cpf']
    email = request.form['email']
    endereco = request.form['endereco']
    bairro = request.form['bairro']
    cep = request.form['cep']
    cidade = request.form['cidade']
    
    db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
    mycursor = db.cursor()
    
    query = 'INSERT INTO mateus_TB_client (cpf, nome, email, endereco, bairro, cep, cidade) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    values = (cpf, nome, email, endereco, bairro, cep, cidade)

    mycursor.execute(query, values)
    db.commit()
    return "Cliente cadastrado!"

app.run(debug=True)
