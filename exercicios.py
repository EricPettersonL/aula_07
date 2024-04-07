#1. Calcular Média de Valores em uma Lista
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

#2. Filtrar Dados Acima de um Limite


def filtra_dados_acima_limite(limite: float, lista: List[float]) -> List[float]:
    '''
    
    função basica para filtrar dados acima de um limite
    '''
    return [x for x in lista if x > limite]

print(filtra_dados_acima_limite(50, lista_numeros))

#3. Contar Valores Únicos em uma Lista

def conta_valores_unicos(lista: List[float]) -> float:
    '''
    função basica para contar valores únicos
    ''' 
    return len(set(lista))
            

print(conta_valores_unicos(lista_numeros))

#4. Converter Celsius para Fahrenheit em uma Lista
def converte_celsius_fahrenheit(celsius: List[float]) -> List[float]:
    '''
    função basica para converter Celsius para Fahrenheit
    '''
    return [x * 1.8 + 32 for x in celsius]

print(converte_celsius_fahrenheit(lista_numeros))

#5. Calcular Desvio Padrão de uma Lista
def calcula_desvio_padrao(lista: List[float]) -> float:
    '''
    função basica para calcular o desvio padrão
    '''
    media = sum(lista) / len(lista)
    return (sum([(x - media) ** 2 for x in lista]) / len(lista)) ** 0.5

print(calcula_desvio_padrao(lista_numeros))

#6. Encontrar Valores Ausentes em uma Sequência
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

print(encontra_valores_ausentes2([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 30, 50]))

