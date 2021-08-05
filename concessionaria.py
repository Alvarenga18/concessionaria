from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'BolaDeCanhão-Supremo'

class Carro:
    def __init__(self, id, marca, modelo, cor, combustivel, ano):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel
        self.ano = ano

c1 = Carro('carro1', 'Ferrari', 'Italia', 'Vermelho', '0,5 L/KM', '2014')
c2 = Carro('carro2', 'Lamborgine', 'Avendador', 'Verde', '0,5 L/KM', '2015')
c3 = Carro('carro3', 'Ferrari', 'LaFerrari', 'Vermelho', '0,5 L/KM', '2016')
c4 = Carro('carro4', 'BMW', 'V8', 'Azul', '0,5 L/KM', '2019')
lista = [c1, c2, c3, c4]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Carros', carros=lista)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proximo=url_for('novo')))
    return render_template('novo.html', titulo='Carro Novo')


@app.route('/criar', methods=['POST',])
def criar():
    id = request.form['id']
    marca = request.form['marca']
    modelo = request.form['modelo']
    cor = request.form['cor']
    combustivel = request.form['combustivel']
    ano = request.form['ano']
    carro = Carro(id, marca, modelo, cor, combustivel, ano)
    lista.append(carro)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo='Login', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if '12345' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + '  Login Cocluído')
        proxima_pagina = request.form['proxima']
        return redirect((proxima_pagina))
    else:
        flash('Usuário ou Senha Incorreta, Tente Novamente')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum Usuário Logado')
    return redirect(url_for('index'))

app.run(debug=True)