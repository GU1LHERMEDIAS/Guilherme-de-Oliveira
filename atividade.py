import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

nome = input('# Insitra seu nome: ')
print('# Olá',nome,'seja Bem Vindo(a)! #')

dados = pd.read_csv('desafio.csv')
print(dados)

media = np.mean(dados)
print('\n# MÉDIA: ',media)

mediana = np.median(dados)
print('\n# MEDIANA: ',mediana)


plt.plot(dados, marker='o', color='red')
plt.show()