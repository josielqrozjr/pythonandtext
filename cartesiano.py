from itertools import product

def processar_linhas_arquivo(nome_arquivo, indices):
    linhas = []

    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    listas_produto_cartesiano = []

    for i in range(0, len(indices), 2):
        indice1, indice2 = indices[i], indices[i + 1]
        linha1 = linhas[indice1].strip()
        linha2 = linhas[indice2].strip()
        lista1 = list(set(linha1.split(', ')))
        lista2 = list(set(linha2.split(', ')))

        lista1 = [int(elemento) for elemento in lista1 if elemento.isdigit()]
        lista2 = [int(elemento) for elemento in lista2 if elemento.isdigit()]

        produto_cartesiano = list(product(lista1, lista2))
        listas_produto_cartesiano.append(produto_cartesiano)

        print(f"Produto Cartesiano: conjunto 1: {{{linha1}}}, conjunto 2: {{{linha2}}}. Resultado: {produto_cartesiano}")

    return listas_produto_cartesiano

prova_dupla = "listacartesiano.txt"
indices_linhas = [2, 3, 5, 6, 8, 9, 11, 12]

listas_produto_cartesiano = processar_linhas_arquivo(prova_dupla, indices_linhas)
