while True:
    jogada1 = input("Jogador 1, escolha pedra, papel ou tesoura: ")
    jogada2 = input("Jogador 2, escolha pedra, papel ou tesoura: ")

    if jogada1 == jogada2:
        print("Empate!")
    elif jogada1 == "pedra":
        if jogada2 == "papel":
            print("Jogador 2 venceu!")
        else:
            print("Jogador 1 venceu!")
    elif jogada1 == "papel":
        if jogada2 == "tesoura":
            print("Jogador 2 venceu!")
        else:
            print("Jogador 1 venceu!")
    elif jogada1 == "tesoura":
        if jogada2 == "pedra":
            print("Jogador 2 venceu!")
        else:
            print("Jogador 1 venceu!")
    else:
        print("Jogada inválida!")

    continuar = input("Quer continuar jogando? (s/n): ")
    if continuar.lower() != "s":
        break