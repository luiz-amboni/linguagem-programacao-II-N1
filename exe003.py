status = True

while True:
    print('Digite uma nota de 0 a 10:')
    nota = int(input())
    if nota >= 0 and nota <= 10:
        break
    else:
        print('Nota inválida !!! Digite uma nota entre 0 e 10')

print("Parabéns, nota certa!")
