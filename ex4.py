import random

while True:
    numero_aleatorio = random.randint(1, 9)
    tentativa = input("Tente adivinhar o número (1-9), ou digite 'sair' para encerrar o jogo: ")

    if tentativa.lower() == "sair":
        break

    try:
        tentativa = int(tentativa)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número entre 1 e 9 ou 'sair'.")
        continue

    if tentativa < 1 or tentativa > 9:
        print("Entrada inválida. Por favor, digite um número entre 1 e 9 ou 'sair'.")
        continue

    if tentativa == numero_aleatorio:
        print("Parabéns! Você acertou o número.")
    elif tentativa < numero_aleatorio:
        print("O número é maior.")
    else:
        print("O número é menor.")
