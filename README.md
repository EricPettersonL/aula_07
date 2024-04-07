# Aula 07 - Funções em Python aula 1

Exercícios realizados para fixação de conteúdo

## 1. Calcular Média de Valores em uma Lista

```python

from typing import List

lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 30, 50]
def calcula_media(lista: List[float]) -> float:
    
    '''
    função basica para calcular a média
    ```
    '''
    
    media = sum(lista) / len(lista)
    return media

print(calcula_media(lista_numeros))

````
## 2. Filtrar Dados Acima de um Limite

```python

def filtra_dados_acima_limite(limite: float, lista: List[float]) -> List[float]:
    '''
    
    função basica para filtrar dados acima de um limite
    '''
    return [x for x in lista if x > limite]

print(filtra_dados_acima_limite(50, lista_numeros))


```
## 3. Contar Valores Únicos em uma Lista

```python
def conta_valores_unicos(lista: List[float]) -> float:
    '''
    função basica para contar valores únicos
    ''' 
    return len(set(lista))
    
print(conta_valores_unicos(lista_numeros))
```

## 4. Converter Celsius para Fahrenheit em uma Lista

```python

def converte_celsius_fahrenheit(celsius: List[float]) -> List[float]:
    '''
    função basica para converter Celsius para Fahrenheit
    '''
    return [x * 1.8 + 32 for x in celsius]

print(converte_celsius_fahrenheit(lista_numeros))

```
## 5. Calcular Desvio Padrão de uma Lista

```python

def calcula_desvio_padrao(lista: List[float]) -> float:
    '''
    função basica para calcular o desvio padrão
    '''
    media = sum(lista) / len(lista)
    return (sum([(x - media) ** 2 for x in lista]) / len(lista)) ** 0.5

print(calcula_desvio_padrao(lista_numeros))

```
## 6. Encontrar Valores Ausentes em uma Sequência

```python

def encontra_valores_ausentes(sequencia: List[float]) -> List[float]:
    '''
    função basica para encontrar valores ausentes
    '''
    return [x for x in sequencia if x is None]

print(encontra_valores_ausentes([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 30, 50, None]))

def encontra_valores_ausentes2(sequencia: List[float]) -> List[float]:
    '''
    função basica para encontrar valores ausentes
    '''
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))

print(encontra_valores_ausentes2(lista_numeros))

```

# Desafio

Criar uma ETL para ler um arquivo .csv, transformar os arquivos (nesse caso ver quais os produtos não foram entregues) e por fim calcular a soma dos produtos entregues, foi realizado em funções onde o arquivo etl.py estão as funções e o main.py e o chamado para realizar a ETL

### ETL

```python

import csv
from typing import List

path_arquivo = 'vendas.csv'
# ler um arquivo .csv
    # entrada: Arquivo .csv
    # saida: Lista de Dicionário de dados
    
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



```

### MAIN

```python
from etl import (ler_arquivo, filtra_produtos_nao_entregues, soma_produtos)


path_arquivo = 'vendas.csv'

lista_produtos = ler_arquivo(path_arquivo)
filtra_produtos_nao_entregues= filtra_produtos_nao_entregues(lista_produtos)  
soma_produtos_entregues = (soma_produtos(lista_produtos))

print(soma_produtos_entregues)

```