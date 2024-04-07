# ler um arquivo .csv
    # entrada: Arquivo .csv
    # saida: Lista de Dicionário de dados
    
import csv
from typing import List

path_arquivo = 'vendas.csv'
def ler_arquivo(arquivo: str) -> List[dict]:
    '''
    função para ler um arquivo .csv
    
    entrada: Arquivo .csv
    
    saida: Lista de Dicionário de dados
    
    '''
    dados = []
    with open(arquivo, mode='r', encoding='utf8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            dados.append(row)
    return dados


# lista de produtos não entregues
    # entrada: Lista de Dicionário de dados
    # saida: Lista de produtos não entregues
    
def filtra_produtos_nao_entregues(dados: List[dict]) -> List[dict]:
    '''
    função para filtrar produtos não entregues
    
    entrada: Lista de Dicionário de dados
    
    saida: Lista de produtos não entregues
    
    '''
    lista_produtos_nao_entregues = []
    for d in dados:
        if d.get('entregue') == 'True':
            lista_produtos_nao_entregues.append(d)
    return lista_produtos_nao_entregues
            

  
    
# soma de valores dos produtos
    # entrada: Dicionário de dados
    # saida: Soma de valores dos produtos que foram entregues 

def soma_produtos(dados: List[dict]) -> float:
    '''
    função para somar os valores dos produtos
    
    entrada: Dicionário de dados
    
    saida: Soma de valores dos produtos
    
    '''
    soma = 0
    for d in dados:
        if d.get('entregue') == 'True':
            soma += float(d.get('price'))
    return soma

