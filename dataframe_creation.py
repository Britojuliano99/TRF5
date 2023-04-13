from clean import limpeza
import pandas as pd
import pdftotext
import re
import os


#Funções usadas no projeto Para Transformar de pdf para Texto e no DataFrame
def transforma_dataframe_novo(lista_arquivos, lista_classe):
  lista_strings = []
  for peticao in lista_arquivos:
    with open(peticao, "rb") as f:
      pdf = pdftotext.PDF(f)
    lista_strings.append("\n\n".join(pdf))
  for i in range(0,len(lista_strings)):
    texto_limpo = limpeza(lista_strings[i])
    texto_limpo.aplicar_limpeza()
    lista_strings[i]=texto_limpo.text

  df = cria_dataframe(lista_arquivos, lista_strings, lista_classe)

  return df

def extrair_nome_path(path):
   padrao=re.compile('[^\\\\/]*$')
   nome_arquivo=padrao.search(path).group()
   return nome_arquivo

def cria_dataframe(lista_arquivos, lista_strings, classificacao):
  nome_arquivos=[]
  for i in range(0,len(lista_arquivos)):
        nome_arquivos.append(extrair_nome_path(lista_arquivos[i]))
        

  
  dicionario_peticao = {
    'nome_documento': nome_arquivos,
    'conteudo_peticao': lista_strings,
    'classificacao': classificacao,
  }
  
  df_peticao_inicial = pd.DataFrame(dicionario_peticao)
  return df_peticao_inicial

def extrair_informação(path):
  file_list = []
  class_list = []

  for dirpath, dirnames, filenames in os.walk(path):
      for file_name in filenames:
          if file_name.endswith(".pdf"):
              full_path = os.path.join(dirpath, file_name)
              file_list.append(full_path)
              class_list.append(os.path.basename(dirpath))

  

  return file_list, class_list

def criar_df(path):
  # aplica a função que extrai as informações do caminho final dos arquivos e a pasta que determina a classe pré-determinada
  lista_arquivos, classe = extrair_informação(path)

  # Aplica a função que ler os textos em pdf e transformas ele em um data_frame com o conteudo dos textos e a determinada classe.
  df=transforma_dataframe_novo(lista_arquivos,classe)

  return df
