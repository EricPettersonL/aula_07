# aula_07
# 1. Calcular Média de Valores em uma Lista

```python
from typing import List

lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 100, 30, 50]
def calcula_media(lista: List[float]) -> float:
    
    '''
    função básica para calcular a média
    '''
    
    media = sum(lista) / len(lista)
    return media

print(calcula_media(lista_numeros))
