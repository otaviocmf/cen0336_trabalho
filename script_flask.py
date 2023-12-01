from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

insetos_cana_de_acucar = [
    {'Nome Científico': 'Atta capiguara', 'É Praga?': True, 'C': 10, 'DE': 30, "Controle Químico": "X",
     "Controle Biológico": "Y", "Controle Cultural": "Z"},
    {'Nome Científico': 'Bolax flavolineatus', 'É Praga?': True, 'C': 0, 'DE': 0, "Controle Químico": "X",
     "Controle Biológico": "Y", "Controle Cultural": "Z"},
    {'Nome Científico': 'Castnia licus', 'É Praga?': True, 'C': 0, 'DE': 0, "Controle Químico": "X",
     "Controle Biológico": "Y", "Controle Cultural": "Z"}
]

def controle_inseto(input_nome, input_numero):
    for inseto in insetos_cana_de_acucar:
        if input_nome == inseto['Nome Científico']:
            if inseto['É Praga?']:
                if input_numero >= inseto['DE']:
                    return "O número de indivíduos atingiu o nível de dano econômico", \
                           {"Controle Químico": inseto['Controle Químico'],
                            "Controle Biológico": inseto['Controle Biológico'],
                            "Controle Cultural": inseto['Controle Cultural']}
                elif inseto['C'] <= input_numero < inseto['DE']:
                    return "O número de indivíduos atingiu o nível de controle.", \
                           {"Controle Químico": inseto['Controle Químico'],
                            "Controle Biológico": inseto['Controle Biológico'],
                            "Controle Cultural": inseto['Controle Cultural']}
                elif input_numero < inseto['C']:
                    return "O número de indivíduos está abaixo do nível de controle."

    return "Inseto não encontrado."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_nome = request.form['input_nome']
        input_numero = int(request.form['input_numero'])
        resultado, controles = controle_inseto(input_nome, input_numero)
        return redirect(url_for('result', resultado=resultado, controles=controles))

    return render_template('main.html')

@app.route('/result')
def result():
    resultado = request.args.get('resultado')
    controles = eval(request.args.get('controles'))
    return render_template('result.html', resultado=resultado, controles=controles)

if __name__ == '__main__':
    app.run(debug=True)
