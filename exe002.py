class Funcionario:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.aumento = 0

    def aumenta_salario(self):
        self.salario = self.salario + self.aumento

class Programador(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 20

class Analista(Funcionario):
    def __init__(self, nome, idade, salario):
        Funcionario.__init__(self, nome, idade, salario)
        self.aumento = 30

programador1 = Programador("Luiz", 19, 3000)
print("\nNome: ", programador1.nome)
print("Salário: ",programador1.salario)
programador1.aumenta_salario()
print("Salário com aumento: ", programador1.salario)


analista1 = Analista("Lucas", 29, 2000)
print("\nNome: ", analista1.nome)
print("Salário: ", analista1.salario)
analista1.aumenta_salario()
print("Salário com aumento: ", analista1.salario)
