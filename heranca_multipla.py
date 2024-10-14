class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f'{self.nome} está amamentando.'

class Ave(Animal):
    def voar(self):
        return f'{self.nome} está voando.'

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return 'Morcegos emitem sons utlrassônicos'


morcego = Morcego('Batman')

# Acessando métodos da classe 'Animal'
print('Nome do morcego: ', morcego.nome)
print('Som do morcego: ', morcego.emitir_som())

# Acessando métodos da classe 'Mamifero' e 'Ave'
print(morcego.amamentar())
print(morcego.voar())
