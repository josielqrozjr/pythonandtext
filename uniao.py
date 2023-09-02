def processar_linhas_arquivo(nome_arquivo, indices):
    linhas = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    listas_uniao = []

    for i in range(0, len(indices), 2):
        indice1, indice2 = indices[i], indices[i + 1]
        linha1 = linhas[indice1].strip()
        linha2 = linhas[indice2].strip()
        uniao = linha1 + ", " + linha2
        lista_uniao = list(set(uniao.split(', ')))

        lista_uniao = [int(elemento) for elemento in lista_uniao if elemento.isdigit()]

        listas_uniao.append(lista_uniao)

        print(f"União: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {lista_uniao}")

    return listas_uniao

prova_dupla = "listauniao.txt"
indices_linhas = [2, 3, 5, 6, 8, 9, 11, 12]

listas_uniao = processar_linhas_arquivo(prova_dupla, indices_linhas)
