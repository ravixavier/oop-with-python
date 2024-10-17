def meu_decorador(func):
    def wrapper():
        print('Antes da funcao ser chamada')
        func()
        print('Depois da funcao ser chamada')
    return wrapper

@meu_decorador
def minha_funcao():
    print('Minha funcao foi chamada')

minha_funcao()

class MeuDecoradorComoClasse:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print('Antes da funcao ser chamada (decorador como classe)')
        self.func()
        print('Antes da funcao ser chamada (decorador como classe)')

@MeuDecoradorComoClasse
def minha_funcao2():
    print('Minha funcao 2 foi chamada')

minha_funcao2()