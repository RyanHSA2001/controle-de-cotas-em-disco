"""
Site do exercício - https://wiki.python.org.br/ListaDeExerciciosProjetos
"""

import pandas as pd
from tabulate import tabulate


def leitura_do_arquivo():

  df = pd.read_csv('usuarios.txt', sep='  ', header=None, engine='python')
  print(tabulate(df, showindex=False, headers=df.columns))


def byte_para_megabyte(byte):
  
  result = byte * 0.000001
  result = float("{:.2f}".format(result))
  return result


def percentual_de_uso(espacoUtilizado, espacoTotalOcupado):

  result  =  (espacoUtilizado / espacoTotalOcupado) * 100
  result = float("{:.2f}".format(result))
  return result
  
  
  
  

print(percentual_de_uso(434.99, 2581.57))
