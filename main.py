from etl import (ler_arquivo, filtra_produtos_nao_entregues, soma_produtos)


path_arquivo = 'vendas.csv'

lista_produtos = ler_arquivo(path_arquivo)
filtra_produtos_nao_entregues= filtra_produtos_nao_entregues(lista_produtos)  
soma_produtos_entregues = (soma_produtos(lista_produtos))

print(soma_produtos_entregues)