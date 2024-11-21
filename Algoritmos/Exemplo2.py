import pandas as pd 
import numpy as np

dados = pd.Series([2,4,6,8,10])

conjunto_dados = np.array(dados)

print(f'Conjunto de dados: {conjunto_dados}')

print(f'Média: {conjunto_dados.mean()}')

print(f'Variância da série de dados: {np.var(conjunto_dados)}')

print(f'Desvio padrão da série de dados: {np.sqrt(conjunto_dados.var)}')

print(f'Desvio padrão da série de dados: {np.std(conjunto_dados)}')

print(f'')