class Controle_Refens:
    def preenche_lista(self):
        lista = []
        cont = 1
        option = 1
        while True:
            lista.append(int(input("Digite o %d° conjunto de refens presos: " % cont)))
            option = int(input("Deseja continuar ? \n[1] - Sim \n[2] - Não \n"))
            cont += 1
            if(option == 2 or option != 1):
                break
        return lista

    def maior(self, lista):
        bigger = lista[0]
        for maior in lista:
            if maior > bigger:
                bigger = maior
        return bigger

    def menor(self, lista):
        smaller = lista[0]
        for menor in lista:
            if menor < smaller:
                smaller = menor
        return smaller

    def soma(self, lista):
        total = 0.0
        for value in lista:
            total += value
        return total

    def calc_media(self, soma_tot, lista):
        average_number = soma_tot / len(lista)
        return average_number

    def calc_media_aproximada(self, media, lista):
        aproximado = {value: abs(value - media) for value in lista}
        return min(aproximado, key=aproximado.get)

num = Controle_Refens()
num_lista = num.preenche_lista()

maior = num.maior(num_lista)
print("Maior conjunto de refens: %d" % maior)

menor = num.menor(num_lista)
print("Menor conjunto de refens: %d" % menor)

soma = num.soma(num_lista)
print("Soma do conjunto de refens: %.2f" % soma)

media = num.calc_media(soma, num_lista)
print("Média do conjunto de refens: %.2f" % media)

media_aproximada = num.calc_media_aproximada(media, num_lista)
print("Valor do conjunto de pressos aproximado da média : %.2f" % media_aproximada)
