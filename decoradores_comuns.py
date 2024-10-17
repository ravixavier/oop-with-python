# @classmethod
# @staticmethod

class MinhaClasse:
    # atributo de classe, nao pode ser acessado diretamente pelo objeto/instancia
    # somente atraves de um methodo do objeto instanciado
    # mas pode ser chamado diretamente pela classe
    atributo = 10

    def __init__(self, nome):
        self.nome = nome # atributo da instancia

    def metodo_instancia(self): # requer uma instancia para ser chamado
        return f'Metodo instancia chamando o atributo da instancia - {self.nome}'

    def metodo_instancia2(self): # requer uma instancia para ser chamado
        return f'Metodo instancia chamando o atributo da classe - {self.atributo}'

    @classmethod
    # um metodo de classe, metodo que eh diretamente ligado a classe
    def metodo_classe(cls):
        return f'Metodo de classe chamando atributo de classe {cls.atributo}'

    @staticmethod
    def metodo_estatico():
        return 'Metodo estatico chamado'


obj = MinhaClasse('Classe exemplo')
print(obj.metodo_instancia())
print(obj.metodo_instancia2())
print(MinhaClasse.atributo)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())


class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, config):
        marca, modelo, ano = config.split(', ')
        return cls(marca, modelo, int(ano))

config1 = 'Honda, HRV, 2024'
carro1 = Carro.criar_carro(config1)
print(f'\nMarca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}\n')

class Matematica:
    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(21, 231))
