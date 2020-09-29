letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def traduz(frase):
    nova_frase = []
    lista_frase = frase.split(',')
    for letra in lista_frase:
        nova_frase.append(letters[int(letra)])
    return ''.join(nova_frase)


while True:
    phrase = input("Digite a mensagem codificada:\n")
    print(traduz(phrase))
