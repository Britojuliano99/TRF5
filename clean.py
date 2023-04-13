import re
import nltk

class limpeza():
    stemmer = nltk.stem.RSLPStemmer()
    stopwords = ['br', 'pág', 'listView', 'https', 'http', 'advogado', 'tabela', 'seguir', 'administrativo', 'processo',
                 'numbr','numbrª', 'ª', 'nº', 'juízo', 'Federal', 'ofício', 'geral', 'defensoria', 'pública', 'união',
                 'justiça', 'federal', 'região', 'pje', 'processo', 'judicial', 'vara', 'subseção', 'judiciária',
                 'juizado', 'especial' , 'cível', 'seção', 'excelentíssimo', 'senhor', 'doutor', 'juiz', 'acórdão',
                 'classe', 'procedimento', 'órgão', 'distribuição', 'excelentissimo', 'gerador', 'fato',
                 'brasileira', 'divorciada', 'servidora', 'cpf', 'residente', 'domiciliada', 'rua',
                 'constituído', 'através', 'procuração', 'anexo', 'vem', 'perante', 'vossa', 'excelência', 'todo', 'acato', 'ajuizar',
                 'presente', 'obrigação', 'fazer', 'pessoa', 'jurídica', 'direito', 'público', 'inscrita', 'cnpj', 'representada', 'localizada',
                 'estado', 'rio', 'grande', 'norte',"oab"]
    def __init__ (self,text):
      self.text=text
      #super.__init__(stopwords)
    def print_texto(self):
      print(self.text)
    def clean_telefone(self):
      regex_telefone = r"\b(\d{2}\)?\s?)?\d{4,5}-?\d{4}\b"
      self.text=re.sub(regex_telefone,"telefone",self.text)
    def clean_espaco(self):
      self.text = re.sub(r'\s+', ' ', self.text) # Substitui o espaço em branco entre os termos por um único espaço
      self.text = re.sub(r'^\s+|\s+?$', '', self.text) # Remova os espaços em branco iniciais e finais
    def clean_urls(self):
      regex_url=r'https?://\S+|www\.\S+'
      self.text = re.sub(regex_url, 'webaddress', self.text) # Substitui URLs por 'webdress'

    def clean_email(self):
      regex_email=r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
      self.text = re.sub(regex_email, 'emailaddress', self.text) # Substitui os endereços de e-mail por 'emailaddress'
       
    def clean_dinheiro(self):
      self.text = re.sub(r'£|\$|r\$', 'moneysymb', self.text) # Substitui os símbolos de dinheiro por 'moneysymb' 
    def clean_pontuacao(self):
      self.text = re.sub('_{1,}', ' ', self.text) #Substitua os '_' por ' '
      self.text = re.sub('[^\w\d\s]', ' ', self.text) # Remover pontuação   
    # Remove as stopwords
    def remove_stopwords(self):
      self.text = ' '.join(word for word in self.text.split(' ') if ((word not in self.stopwords) and (len(word) > 2 )))  # retira stopwords e palavras com menos de 3 letras

    # Função de stematizar o texto, deixando as palavras somente com radicais
    def stemming(self):
      palavras=[]
      for w in self.text.split():
          palavras.append(self.stemmer.stem(w))
      texto_stemming= " ".join(palavras)
      self.text=texto_stemming
    
    
    def aplicar_limpeza(self):
      self.remove_header_footer()
      self.clean_espaco()
      self.clean_urls()
      self.clean_email()
      self.clean_dinheiro()
      self.clean_telefone()
      self.clean_pontuacao()
      self.remove_stopwords()
      self.stemming()
      

    # Função de remover cabeçalho e rodapé
    def remove_header_footer(self):
      '''Remoção dos cabeçalhos e rodapé do texto da petição'''
      #Verifica se a entrada em uma string ou uma lista
      if isinstance(self.text, str) == False:
          return 'Entrada não é uma str'
      
      list_of_pages = [self.text]

      # Dividi o texto em cada quebra de linha '\n'
      input_split = [
          p.split("\n") for p in list_of_pages
      ]
      #Removendo espaços em branco extras
      for i in range(len(input_split)):
          input_split[i] = list(map(str.strip, input_split[i]))


      #Contar o numero de ocorrencia de cada linha
      counts = {}
      for i in input_split[0]:
          counts[i] = counts.get(i, 0) + 1
      commum_lines = [key for key, value in counts.items() if value >= 2]

      input_split_fixed = []

      for page in input_split:
          text = [i for i in page if i not in commum_lines]
          input_split_fixed.append("\n".join(text))

      self.text='\n'.join(input_split_fixed)
        
