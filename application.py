"""
Site do exercício - https://wiki.python.org.br/ListaDeExerciciosProjetos
"""

import pandas as pd


def leitura_do_arquivo():

  df = pd.read_csv('usuarios.txt', sep='  ', header=None, engine='python')
  # df = tabulate(df, showindex=True, headers=df.columns)

  return df


def byte_para_megabyte(byte):
  
  result = byte * 0.000001
  result = float("{:.2f}".format(result))
  return result


def percentual_de_uso(espacoUtilizado, espacoTotalOcupado):

  result  =  (espacoUtilizado / espacoTotalOcupado) * 100
  result = float("{:.2f}".format(result))
  return result
  

def impressao(df):

  # relatorio = f"""
  # ACME Inc.                   Uso do espaço em disco pelos usuários
  # -----------------------------------------------------------------
  # Nr.          Usuário          Espaço utilizado          % do uso
  # {df[0][1]}


  relatorio = pd.DataFrame(columns=['Nr.', ' Usuário',  'Espaço utilizado',  '% do uso'])

  usuarios = df[df.columns[0]].count()

  sum = 0
  
  for i in range(usuarios):
    sum += df[1][i]

  espacoTotalOcupado = byte_para_megabyte(sum)
  
  for i in range(usuarios):
    relatorio.loc[i] = [i+1, df[0][i], str(byte_para_megabyte(df[1][i])) + " MB", str(percentual_de_uso(byte_para_megabyte(df[1][i]), espacoTotalOcupado)) + " %"]
 
  
  print(relatorio)
  

  