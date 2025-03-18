import numpy as np

data = np.loadtxt('annual-co2-emissions.csv', delimiter=',', usecols=(3), skiprows=1)
print(data)