nome_arquivo = "nomes.txt"
frequencia_nomes = {}

with open(nome_arquivo, "r") as arquivo:
    for linha in arquivo:
        nomes = linha.strip().split()
        for nome in nomes:
            if nome in frequencia_nomes:
                frequencia_nomes[nome] += 1
            else:
                frequencia_nomes[nome] = 1

for nome, frequencia in frequencia_nomes.items():

        print(nome, frequencia)
