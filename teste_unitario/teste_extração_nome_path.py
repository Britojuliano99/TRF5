from dataframe_creation import *

path='/home/juliano/TRF5/trf5.peticoes/20 - APOSENTADORIA POR IDADE HÍBRIDA (URBANA-RURAL)/0000087-79.2023.4.05.8307.pdf'
path_extraido_certo='0000087-79.2023.4.05.8307.pdf'    



path_extraido=extrair_nome_path(path)

if path_extraido== path_extraido_certo:
    print("Passou no teste")
    print(path_extraido)
else:
    print("Errado")
