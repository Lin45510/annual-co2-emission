import numpy as np

data = np.loadtxt('annual-co2-emissions.csv', delimiter=',', usecols=(3), skiprows=1)

print('Dados sobre a Emissão de CO² entre 1750 e 2023')

#Media
print(f'Media: {np.mean(data):.2f}')

#Mediana
print(f'Mediana: {np.median(data):.2f}')

#Desvio padrão
print(f'Desvio Padrão: {np.std(data):.2f}')

#Maxima e Minima
print(f'Maxima: {data.max()} | Minima: {data.min()}')