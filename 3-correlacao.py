
"""
a correlacao tem uma escala de 1 positivo e -1 negativo e tem o 0 no meio,
e usada para dizer se uma variavel esplica a aoutra variavel,
tipo se uma varuialvel sobe a outra tambem deve subir e vise versa

escala
-------------------------
 1.0 => plena
 0.7 => forte
 0.5 => moderada
 0.2 => fraca
0 => inesistente
- 0.2 => fraca
- 0.5 => moderada
- 0.7 => forte
- 1.0 => plena
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

base_data = pd.read_excel('BaseDados_RegressaoLinear.xlsx', 'Plan1')

Eixo_x = base_data.iloc[:, 0].values
Eixo_y = base_data.iloc[:, 1].values

correlacao = np.corrcoef(Eixo_x, Eixo_y)

plt.figure(figsize=(10, 5))
sns.heatmap(correlacao, annot=True)
# annot=True mostra os valores no meio do grafico
# mostra as variacoes de todas as variaveis
plt.show()

