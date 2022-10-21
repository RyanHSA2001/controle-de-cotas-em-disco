"""
Site do exercício - https://wiki.python.org.br/ListaDeExerciciosProjetos
"""

import pandas as pd
from tabulate import tabulate


def leitura_do_arquivo():

  df = pd.read_csv('usuarios.txt', sep='  ', header=None, engine='python')
  

  return df


def byte_para_megabyte(byte):
  
  result = byte * 0.000001
  result = float("{:.2f}".format(result))
  return result


def percentual_de_uso(espacoUtilizado, espacoTotalOcupado):

  result  =  (espacoUtilizado / espacoTotalOcupado) * 100
  result = float("{:.2f}".format(result))
  return result

def prefixar_espaços_nas_colunas(df: pd.DataFrame, n):
  spaces = ' ' * n

  if isinstance(df.columns.nlevels, pd.MultiIndex):
    for i in range(df.columns.nlevels):
      levelNew = [spaces + str(s) for s in df.columns.levels[i]]
      df.columns.set_levels(levelNew, level=i, inplace=True)
  else:
    df.columns = spaces + df.columns

  df = df.astype(str)
  df = spaces + df

  return df

def impressao(df):

  header = """
  ACME Inc.             Uso do espaço em disco pelos usuários
  -----------------------------------------------------------
  \n"""
  
  f = open('relatorio.txt', 'x')
  f.write(header)
  f.close
  

  relatorio = pd.DataFrame(columns=['Nr.', ' Usuário',  'Espaço utilizado',  '% do uso'])

  usuarios = df[df.columns[0]].count()

  sum = 0
  
  for i in range(usuarios):
    sum += df[1][i]

  espacoTotalOcupado = byte_para_megabyte(sum)
  
  for i in range(usuarios):
    relatorio.loc[i] = [i+1, df[0][i], str(byte_para_megabyte(df[1][i])) + " MB", str(percentual_de_uso(byte_para_megabyte(df[1][i]), espacoTotalOcupado)) + " %"]

  relatorio = prefixar_espaços_nas_colunas(relatorio, 3)
  
  relatorio = tabulate(relatorio, showindex=False, headers=relatorio.columns, tablefmt= "plain", stralign= ("right"))

  espacoMedio = espacoTotalOcupado/usuarios
  espacoMedio = float("{:.2f}".format(espacoMedio))

  
  f = open('relatorio.txt', 'a')
  f.write(relatorio)
  f.write(f"""
    
    Espaço total ocupado: {espacoTotalOcupado} MB
    Espaço médio ocupado: {espacoMedio} MB""")
  f.close

  f = open('relatorio.txt', 'r')
  print(f.read())
  f.close
  

  