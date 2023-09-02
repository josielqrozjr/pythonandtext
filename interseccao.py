def processar_linhas_arquivo(nome_arquivo, indices):
    linhas = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    listas_intersecao = []

    for i in range(0, len(indices), 2):
        indice1, indice2 = indices[i], indices[i + 1]
        linha1 = linhas[indice1].strip()
        linha2 = linhas[indice2].strip()
        lista1 = list(set(linha1.split(', ')))
        lista2 = list(set(linha2.split(', ')))

        lista1 = [int(elemento) for elemento in lista1 if elemento.isdigit()]
        lista2 = [int(elemento) for elemento in lista2 if elemento.isdigit()]

        intersecao = list(set(lista1).intersection(lista2))
        listas_intersecao.append(intersecao)

        print(f"Interseção: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {intersecao}")

    return listas_intersecao

prova_dupla = "listainterseccao.txt"
indices_linhas = [2, 3, 5, 6, 8, 9, 11, 12]

listas_intersecao = processar_linhas_arquivo(prova_dupla, indices_linhas)
