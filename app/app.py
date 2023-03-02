from flask import Flask, render_template, request
from fun import cifrar, de_cifrar, enigma, de_enigma

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')
    

# Rota para a página do enigma
@app.route('/enigma', methods=['GET', 'POST'])
def enigma_view():
    if request.method == 'POST':
        msg = request.form['msg']
        # Criar o P e o E aqui e passar para a função enigma
        # cifrada = enigma(msg)
        return render_template('enigma.html', cifrada=msg)
    return render_template('enigma.html')

# Rota para a página de decifrar o enigma
@app.route('/de_enigma', methods=['GET', 'POST'])
def de_enigma_view():
    if request.method == 'POST':
        msg = request.form['msg']
        decifrada = de_enigma(msg)
        return render_template('de_enigma.html', decifrada=decifrada)
    return render_template('de_enigma.html')

if __name__ == '__main__':
    app.run(debug=True)