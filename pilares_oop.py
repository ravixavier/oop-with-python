#Exemplo de Hereditariedade

class Animal:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def andar(self):
        print(f'The Animal {self.name}, walks')

    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return 'raw, raw!'

class Cat(Animal):
    def make_sound(self):
        return 'eow, eow, eow...'


dog1 = Dog('Bart', 10)
cat1 = Cat('Linda', 2)

print(f'Exemplo de poliformismo')

animals = [dog1, cat1]

for animal in animals:
    print(f'{animal.name} faz: {animal.make_sound()}')

print(f'\nExemplo de Encapsulamento')
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo #Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo

minha_conta = ContaBancaria(1000)
print(f"Saldo da conta bancária: {minha_conta.consultar_saldo()}")
minha_conta.depositar(700)
print(f"Saldo da conta bancária: {minha_conta.consultar_saldo()}")
minha_conta.depositar(-239)
print(f"Saldo da conta bancária: {minha_conta.consultar_saldo()}")
minha_conta.sacar(150)
print(f"Saldo da conta bancária: {minha_conta.consultar_saldo()}")

print("\nExemplo de abstração: ")
from abc import ABC, abstractmethod

# Classe abstrata (não pode ser instanciada)
class Veiculo(ABC):

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def ligar(self):
        print("O veiculo está ligado.")

# Classe concreta que herda de veiculo
class Carro(Veiculo, ABC):
    def acelerar(self):
        print('O carro está acelerando.')

    def frear(self):
        print('O carro está freando.')


class Moto(Veiculo, ABC):
    def acelerar(self):
        print('O moto está acelerando.')

    def frear(self):
        print('O moto está freando.')

