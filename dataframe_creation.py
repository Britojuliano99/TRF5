from limpeza import limpeza
import pandas as pd
import pdftotext
import re

#Funções usadas no projeto Para Transformar de pdf para Texto e no DataFrame
def transforma_dataframe_novo(lista_arquivos, classe):
  lista_strings = []
  for peticao in lista_arquivos:
    with open(peticao, "rb") as f:
      pdf = pdftotext.PDF(f)
    lista_strings.append("\n\n".join(pdf))
  for i in range(0,len(lista_strings)):
    texto_limpo = limpeza(lista_strings[i])
    texto_limpo.aplicar_limpeza()
    lista_strings[i]=texto_limpo.text
  classificacao = []
  for i in range(len(lista_arquivos)):
    classificacao.append(classe)

  df = cria_dataframe(lista_arquivos, lista_strings, classificacao)
  return df

def extrair_nome_path(path):
   padrao=re.compile('[^\\\\/]*$')
   nome_arquivo=padrao.search(path).group()
   return nome_arquivo

def cria_dataframe(lista_arquivos, lista_strings, classificacao):
  nome_arquivos=[]
  for i in range(0,len(lista_arquivos)):
        nome_arquivos.append(extrair_nome_path(lista_arquivos[i]))
        print(nome_arquivos[i])

  
  dicionario_peticao = {
    'nome_documento': nome_arquivos,
    'conteudo_peticao': lista_strings,
    'classificacao': classificacao,
  }
  
  df_peticao_inicial = pd.DataFrame(dicionario_peticao)
  return df_peticao_inicial