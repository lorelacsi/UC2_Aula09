import pandas as pd 
import numpy as np

idades = pd.Series([5,10,12,35,38])

conjunto_idades = np.array(idades)

med_idades = conjunto_idades.mean()
var_idades = np.var(conjunto_idades)
desvio_idades = np.std(conjunto_idades)

print(f'Conjunto de dados: {conjunto_idades}')

print(f'Média: {med_idades.mean()}')

print(f'Variância da série de idades: {np.var(var_idades)}')

distancia_var_media = var_idades / (med_idades ** 2)
print(f'Distância entre a variância e a média: {distancia_var_media}')

coef_variacao = (desvio_idades / med_idades) * 100
print(f'Coeficiente de variacao: {coef_variacao}')

variancia_amostral = np.var(conjunto_idades, ddof=1)
print(f'Variancia amostral: {variancia_amostral}')

desvio_padrao_amostral = np.std(conjunto_idades, ddof=1)
print(f'Desvio Padrão entre as idades {desvio_padrao_amostral}')