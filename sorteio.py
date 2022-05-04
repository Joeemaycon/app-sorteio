import time
import random

for tentativas in range(5):
    valor_desejado = int(input('Digite um Valor de 1 a 5: '))
    valor_da_sorte = random.randint(1, 5)
    if valor_desejado == valor_da_sorte:
        print('Ganhooooouuuuu')
        time.sleep(3)  # funciona com IMPORT time
        break

    elif valor_desejado >= 6:
        print('Perdeu uma chance somente valores de 1 a 5')
    else:
        print('Não foi dessa vez.')
