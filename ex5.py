def remove_duplicatas(lista):
    nova_lista = []
    for elemento in lista:
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista
