"""
Site do exercício - https://wiki.python.org.br/ListaDeExerciciosProjetos
"""

import pandas as pd
from tabulate import tabulate


def leitura_do_arquivo(
):  # Lê o arquivo usuarios.txt e retorna um dataframe pandas.
  
  df = pd.read_csv('usuarios.txt', sep='  ', header=None, engine='python')

  return df


def byte_para_megabyte(
    byte):  # Converte bytes para megabytes e retorna o resultado.

  result = byte * 0.000001
  result = float("{:.2f}".format(result))
  return result


def percentual_de_uso(
    espacoUtilizado,
    espacoTotalOcupado):  # Calcula o percentual de uso de cada usuário.

  result = (espacoUtilizado / espacoTotalOcupado) * 100
  result = float("{:.2f}".format(result))
  return result


def prefixar_espaços_nas_colunas(
  df: pd.DataFrame, n
):  # Formata o dataframe, colocando 3 ou n espaços entre cada coluna. Retorna o dataframe.
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


def impressao(
    df):  # Trata os dados iterando sobre o dataframe e gera o relatório.

  header = """
   ACME Inc.             Uso do espaço em disco pelos usuários
   -----------------------------------------------------------
  \n"""
      
  try:
    f = open('relatorio.txt', 'x')
    f.write(header)
    f.close
  except:
    print("Arquivo relatorio.txt já existe")
    
    return False
  

  relatorio = pd.DataFrame(columns=['Nr.', ' Usuário', 'Espaço utilizado', '% do uso'])
  dash = pd.DataFrame(columns=['Nr.', 'Usuário', 'Espaço Utilizado', '% do uso'])

  quantidadeUsuarios = df[df.columns[0]].count()

  usuarios = []
  for i in range(
      quantidadeUsuarios):  # Ordena os usuários em odem descrescente

    usuarios.append(df[1][i])

  usuarios = sorted(usuarios)
  usuariosCrescente = usuarios.reverse()

  sum = 0

  for i in range(
      quantidadeUsuarios):  # Soma o espaço utilizado pelos usuários.
    sum += df[1][i]

  espacoTotalOcupado = byte_para_megabyte(sum)

  for i in range(quantidadeUsuarios):  # Adiciona os dados ao relatório.
    for j in range(quantidadeUsuarios):
      if byte_para_megabyte(usuarios[i]) == byte_para_megabyte(df[1][j]):

        relatorio.loc[i] = [
          i + 1, df[0][j],
          str(byte_para_megabyte(df[1][j])) + " MB",
          str(
            percentual_de_uso(byte_para_megabyte(df[1][j]),
                              espacoTotalOcupado)) + " %"
        ]
        dash.loc[i] = [i + 1, df[0][j], byte_para_megabyte(df[1][j]),
                       percentual_de_uso(byte_para_megabyte(df[1][j]), espacoTotalOcupado)]

  relatorio = prefixar_espaços_nas_colunas(relatorio, 3)

  relatorio = tabulate(relatorio,
                       showindex=False,
                       headers=relatorio.columns,
                       tablefmt="plain",
                       stralign=("right"))

  espacoMedio = espacoTotalOcupado / quantidadeUsuarios
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

  dash.to_csv('toDash.csv', index=False)

