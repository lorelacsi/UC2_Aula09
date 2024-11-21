# Variancia

# Média dos quadrados das diferenças entre cada valor e a média, o resultado é elevado ao quadrado
# Soma os quadrados das diferenças entre cada valor e média, dividindo pelo número de elementos

# varianca = np.var

# Desvio adrão

# Raiz quadrada da variância
# Apresenta o quanto os dados estão afastados da média
# Se o desvio for alto, os dados estão espalhados, se for menor, os dados estão próximos da média
# desvio_padrao = np.std

dados = {1 , 2, 3, 4, 5}

media = sum (dados) / len(dados)
print(f'Media: {media}')

diferencas = [x - media for x in dados]
print(f'Diferenças em relação a média: {diferencas}')

quadrados_diferencas = [x**2 for x in diferencas]
print(f'Quadrados das diferencas: {quadrados_diferencas }')

media_quadrados_diferencas = sum(quadrados_diferencas) / len(quadrados_diferencas)
print(f'Variância é a média dos quadrados das difrenças: {media_quadrados_diferencas}')

desvio_padrao = media_quadrados_diferencas ** 0.5
print(f'Desvio padrão é a raiz quadrada da variância: {desvio_padrao}')


