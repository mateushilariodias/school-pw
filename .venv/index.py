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

@app.route('/cadastro_usuario', methods=['POST'])
def inserir_usuario():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = request.form['senha']
    
    db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
    mycursor = db.cursor()
    
    query = 'INSERT INTO mateus_TB_user (usuario, email, senha) VALUES (%s,%s,%s)'
    values = (usuario, email, senha)
    
    mycursor.execute(query, values)
    
    db.commit()
    return redirect(url_for('cadastroDeCliente'))

@app.route('/cadastro-usuario')
def cadastroDeUsuario():
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
        mycursor = db.cursor()
        query='select usuario, email from mateus_TB_user'
        mycursor.execute(query)
        resultado = mycursor.fetchall()
        return render_template('cadastro-usuario.html', usuarios = resultado)

@app.route('/cadastro_cliente', methods=['POST'])
def inserir_cliente():
    cpf = request.form['cpf']
    nome = request.form['nome']
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
    return redirect(url_for('cadastroDeCliente'))

@app.route('/cadastro-cliente')
def cadastroDeCliente():
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
        
        mycursor = db.cursor()
        query='select * from mateus_TB_client'
        mycursor.execute(query)
        resultado = mycursor.fetchall()
        return render_template('cadastro-cliente.html', titulo = 'Cadastrar Cliente', cpfs = resultado)          

@app.route('/excluir-usuario/<usuario>')
def excluirUsuario(usuario):
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
        mycursor = db.cursor()
        query="delete from mateus_TB_user where usuario = '" + usuario + "'"
        mycursor.execute(query)
        db.commit()
        return redirect(url_for('cadastro-usuario'))

@app.route('/atualizar-usuario/<usuario>')
def atualizarUsuario(usuario):
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
        mycursor = db.cursor()
        query="select usuario, email, senha from mateus_TB_user where usuario = '" + usuario + "'"
        mycursor.execute(query)
        resultado = mycursor.fetchall()
        return render_template('atualizar_usuario.html', usuarios = resultado)

@app.route('/salvar_alteracao_usuario', methods=['POST'])
def salvarAlteracaoUsuario():
        usuario = request.form['usuario']
        email = request.form['email']
        senha = request.form['senha']

        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
        
        mycursor = db.cursor()
        query="update mateus_TB_user set usuario = '"+ usuario +"', senha = '"+ senha +"', email = '"+ email +"' where usuario = '"+ usuario +"'"
        mycursor.execute(query)
        db.commit()
        return redirect(url_for('cadastroDeUsuario'))

@app.route('/excluir-cliente/<cpf>')
def excluirCliente(cpf):
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
        mycursor = db.cursor()
        query="delete from mateus_TB_client where cpf = '" + cpf + "'"
        mycursor.execute(query)
        db.commit()
        return redirect(url_for('cadastro-cliente'))


@app.route('/atualizar-cliente/<cpf>')
def atualizarCliente(cpf):
        db = mysql.connector.connect(host='mysql01.cgkdrobnydiy.us-east-1.rds.amazonaws.com',
                                 user='aluno_fatec',
                                 password='aluno_fatec',
                                 database='meu_banco')
    
        mycursor = db.cursor()
        query="select cpf, nome, email, endereco, bairro, cep, cidade from mateus_TB_client where cpf = '" + cpf + "'"
        mycursor.execute(query)
        resultado = mycursor.fetchall()
        return render_template('atualizar_cliente.html', cpfs = resultado)

@app.route('/salvar_alteracao_cliente', methods=['POST'])
def salvarAlteracaoCliente():
        cpf = request.form['cpf']
        nome = request.form['nome']
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
        query="update mateus_TB_client set cpf = '"+ cpf +"', nome = '"+ nome +"', email = '"+ email +"', endereco = '"+ endereco +"', bairro = '"+ bairro +"', cep = '"+ cep +"', cidade = '"+ cidade +"' where cpf = '" + cpf + "'"
        mycursor.execute(query)
        db.commit()
        return redirect(url_for('cadastroDeCliente'))

app.run(debug=True)
