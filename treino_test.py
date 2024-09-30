import pandas as pd

base_data = pd.read_excel('BaseDados_RegressaoLinear.xlsx', 'Plan1')

Eixo_x = base_data.iloc[:, 0].values
Eixo_y = base_data.iloc[:, 1].values

Eixo_y = Eixo_y.reshape(-1, 1)
Eixo_x = Eixo_x.reshape(-1, 1)
