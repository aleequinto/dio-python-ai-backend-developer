class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('Bibi')
    
    def parar(self):
        print('PARAA BICICLETINHA')
        print('*parada*')

    def correr(self):
        print('*dando grau*')

b1 = Bicicleta('vermelha', 'caloi', 2022, 600)