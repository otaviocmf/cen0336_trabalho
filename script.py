import sys
input_nome = 'Atta capiguara'
input_numero = 30

insetos_cana_de_acucar = [
    #'<C': abaixo do nível de controle
    #'C': nivel de controle
    #'DE': dano econômico
    {'Nome Científico': 'Atta capiguara', 'É Praga?': True, 'C': 10, 'DE': 30, "Controle Químico": "X", "Controle Biológico": "Y", "Controle Cultural": "Z"},
    {'Nome Científico': 'Bolax flavolineatus', 'É Praga?': True, 'C': 0, 'DE': 0, "Controle Químico": "X", "Controle Biológico": "Y", "Controle Cultural": "Z"},
    {'Nome Científico': 'Castnia licus', 'É Praga?': True, 'C': 0, 'DE': 0, "Controle Químico": "X", "Controle Biológico": "Y", "Controle Cultural": "Z"}
]

for inseto in insetos_cana_de_acucar:
    if input_nome == inseto['Nome Científico']:
        if inseto['É Praga?']:
            if input_numero >= inseto['DE']:
                print("O número de indivíduos atingiu o nível de dano econômico")
                print("As opções de controle para essa praga são:")
                print("Controle Químico:", inseto['Controle Químico'])
                print("Controle Biológico:", inseto['Controle Biológico'])
                print("Controle Cultural:", inseto['Controle Cultural'])

            elif inseto['C'] <= input_numero < inseto['DE']:
                print("O número de indivíduos atingiu o nível de controle.")
                print("As opções de controle para essa praga são:")
                print("Controle Químico:", inseto['Controle Químico'])
                print("Controle Biológico:", inseto['Controle Biológico'])
                print("Controle Cultural:", inseto['Controle Cultural'])

            elif input_numero < inseto['C']:
                print("O número de indivíduos está abaixo do nível de controle.")