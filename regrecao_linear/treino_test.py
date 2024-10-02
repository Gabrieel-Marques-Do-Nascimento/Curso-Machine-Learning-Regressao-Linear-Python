import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

base_data = pd.read_excel('BaseDados_RegressaoLinear.xlsx', 'Plan1')

Eixo_x = base_data.iloc[:, 0].values
Eixo_y = base_data.iloc[:, 1].values

Eixo_y = Eixo_y.reshape(-1, 1)
Eixo_x = Eixo_x.reshape(-1, 1)

# vai dividir os dados em dados de teste e traino
# vai usar esses dados para previzao e tambem serao usados para verificar se estao corretos
x_train, x_test, y_train, y_test = train_test_split(
    Eixo_x, Eixo_y,
    test_size=0.20  # 20% dos dados serao para test
)

# nesse exemplo vamos usar 20% mais com uma grande qunatidade de dados usar 25% a 30% dos dados para teste
# print(len(x_train), len(x_test))  # 79 20


# caculos estatisticos da regrecao linear
funcao_Regrecao = LinearRegression()
# fit vai aplicar todos os calculos ewtatisticos para treinar o modelo
funcao_Regrecao.fit(x_train, y_train)
# apos executar o modelo serar treinado

# score e procimo da correlacao
funcao_Regrecao.score(x_train, y_train)

#
plt.figure(figsize=(10, 5))
plt.scatter(x_train, y_train)
plt.plot(x_test, funcao_Regrecao.predict(x_test), color='red')
# predict fas previsoes
plt.show()

previsoes = funcao_Regrecao.predict(x_test)
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, previsoes)))

# fornula estatistica
#
# RMSE =


print( funcao_Regrecao.predict([[5500]]))
