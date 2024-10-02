import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

base_data = pd.read_excel('BaseDados_RegressaoLinear.xlsx', 'Plan1')
# print(base_data.tail(5)) # mostra os ultimos 5 items
#         Salario  Limite_Emprestimo
# 94  3185.629581        7279.937858
# 95  3217.485877        7315.799621
# 96  3249.660736        7351.661384
# 97  3282.157343        7387.523147
# 98  3314.978916        7423.384910

# print(base_data.columns) # mostra os nomes das columns
# Index(['Salario', 'Limite_Emprestimo'], dtype='object')

# print(base_data.info()) # mostra uma lista de columns, o numero de valores, e formato dos campos
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 99 entries, 0 to 98
# Data columns (total 2 columns):
#  #   Column             Non-Null Count  Dtype
# ---  ------             --------------  -----
#  0   Salario            99 non-null     float64
#  1   Limite_Emprestimo  99 non-null     float64
# dtypes: float64(2)
# memory usage: 1.7 KB
# None

# print(base_data.describe())
#            Salario  Limite_Emprestimo
# count    99.000000          99.000000
# mean   2119.100581        4900.652060
# std     600.832983        1378.113961  # desvio da media
# min    1250.219130        2900.124323
# 25%    1595.383780        3700.800280
# 50%    2035.792243        4722.412623
# 75%    2597.840528        6026.191986
# max    3314.978916        7423.384910


# converter para um array
# ":" reference a todos os item da column, "0" e a column no caso a primeira
Eixo_x = base_data.iloc[:, 0].values
Eixo_y = base_data.iloc[:, 1].values
# converted para array e melhor para performance

# primeira visualizacao grasfica
# figsize=(horizontal, vertical)
plt.figure(figsize=(10, 5))
# funcao de um grafico
# vai pedir tanto o valor x quanto o valor y
plt.scatter(Eixo_x, Eixo_y)
plt.title('Grafico com dois eixos')
plt.xlabel("salario")
plt.ylabel('limit')
# plt.show()
# ficou pronta a primeira analize grafica do nossos dados

# define um grafico com essas dimensoes
plt.figure(figsize=(10, 5))
# chama o grafico heachmap com a base_data.isnull()  isnull detequita valor's nulls
# se tiver algum valor null no grafico vermelho vai aparecer um listra branca
sns.heatmap(base_data.isnull())
# se a base for grande vai demorar para rodar,
# pega toda a base de dados e fas um grafico de dois eixos para todas as variaveis,
# tipo sao dois graficos para cada column
# nao usavel e dados muinto grandes
sns.pairplot(base_data)
plt.show()

# correlacao dos dados
correlacao = np.corrcoef(Eixo_x, Eixo_y)
# o numpy calcul;a a correlacao
print("correlacao:\n", correlacao)  # 0.99949773
