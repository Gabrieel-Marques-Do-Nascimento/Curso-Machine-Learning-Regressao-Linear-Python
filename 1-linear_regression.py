"""
calculos estaticos de regrecao linear

formula matematica

>> y = a.x + b
"""
import pandas as pd

data = {"Apartamento": ['apto 01', 'apto 02', 'apto 03', 'apto 04', 'apto 05', "totais"],
        "metragem (X)": [45, 50, 55, 60, 65, 275],
        "preco (y)": [210.950, 250.250, 380.670, 410.200, 450.900, 1_702.970],
        "totais": [275, 1_702.970]}



del data["totais"]
tabeal_data = pd.DataFrame(data)
# print(tabeal_data)
"""
     Apartamento   metragem (X)   preco (y)
0     apto 01            45     210.95
1     apto 02            50     250.25
2     apto 03            55     380.67
3     apto 04            60     410.20
4     apto 05            65     450.90
5      totais           275    1702.97

aqui temos um lista simples de apartamentos, metragem, e preco e no final de cada coluna tem  a soma de todos 
os valores, primeiro pegar cada item da coluna x e multplicar pelo item correspondente da  coluna y
e no final tem a soma de todos os valores

fromula: x.y
"""
data['x.y'] = []
total = 0
for ind, item in enumerate(data['metragem (X)'][:-1]):
    total += item * data["preco (y)"][ind]
    data['x*y'].append(item * data["preco (y)"][ind])
data['x2'].append(total)
# print(data)
"""
>>>          Apartamento  metragem (X)  preco (y)   x*y
>>>      0     apto 01            45     210.95    9492.75
>>>      1     apto 02            50     250.25   12512.50
>>>      2     apto 03            55     380.67   20936.85
>>>      3     apto 04            60     410.20   24612.00
>>>      4     apto 05            65     450.90   29308.50
>>>      5      totais           275    1.702.97  96.862.600

agora e pegar os dados da coluna x e elecar ao quadrado: X²
e somar todos os valores 
"""
data['x2'] = []
total = 0
for item in data['metragem (X)'][:-1]:
    total += item
    data['x2'].append( item ** 2)
data['x2'].append(total)
"""
  Apartamento  metragem (X)  preco (y)     x.y        x2
0     apto 01          45     210.95     9492.75      2025
1     apto 02          50     250.25     12512.50     2500
2     apto 03          55     380.67     20936.85     3025
3     apto 04          60     410.20     24612.00     3600
4     apto 05          65     450.90     29308.50     4225
5     totais           275    1.702.97   96.862.600   15.375

"""
# depois de tudo isso vamos calcular o valor de `a` que fas parte da formula la no cabecalho
# m    = quantidade de registros ==  5
# ∑x.y =  a soma da coluna x.y   ==  96.862.600
# ∑x   =  a soma da coluna x     ==  275
# ∑y   =  a soma da coluna y     ==  702.97

# >>         m. ∑x.y - ∑x . ∑y                  5 * 96.862.600 - 275 * 1.702.97             15.996.250
# >> a =  ------------------------   ==   --------------------------------------------  =  ---------------- = 12.797
# >>         m. ∑x² - ( ∑x)²                        5 * 15.375 - (275)²                         1.250
# o valor de `a` e  12.797

# agora temos que descobrir o valor de `b`
# b == a media da coluna y menos  `a` vezes a media da coluna x
# obs: soma dos valores dividido pelo numero de valores ex:  275 / 5
# b = y_media - `a` * x_media == b = 340.594 - `a` * 55   ==   340.594 - 12.797 * 55  = -363.241
# o valor de `b` e  -363.241
# >> y = a.x + b ==  y = 12.797 .x -363.241

# PREVIZOES
# APARTAMENTO DE 67 METROS E   APARTAMENTO DE 42 METROS
# agora e so substituir x pelo valor que quer prever
# >> y = a.x + b == y = 12.797 .x -363.241 ==  y = 12.797 * 67 - 363.241  = 494.158
# >> y = 12.797 * 42 - 363.241 = 174.233



