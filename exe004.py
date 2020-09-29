import datetime
import random

#O decorador é um padrão usado quando você precisa anexar responsabilidades dinamicamente sem precisar de uma grande hierarquia de subclasses.
#Decorator nada mais é que um método para envolver uma função, modificando seu comportamento.
#Em Engenharia de Software, um padrão de projeto é uma solução geral para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software.

def calcula_tempo_decorator(function):
    def calcula_tempo():
        print(datetime.datetime.now())
        function()
        print(datetime.datetime.now())
    return calcula_tempo

@calcula_tempo_decorator
def soma_num_aleatorio():

    soma = random.randint(0, 10) + random.randint(0, 10) + random.randint(0, 10) + random.randint(0, 10) + random.randint(0, 10)
    print(soma)

soma_num_aleatorio()

""" https://medium.com/@giselezrossi/decorator-with-python-dba2016706cf """
