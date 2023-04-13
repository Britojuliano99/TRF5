from clean import limpeza

texto=" Bom dia dajdpadp eu sou juliano@brito.com www.gmail.com $ $ 83123 asd palavras masculino feminino."
texto_limpo="bom dia dajdpadp sou emailaddres webaddres moneysymb moneysymb 83123 asd palavr masculin feminin"
A=limpeza(texto)
A.aplicar_limpeza()

if A.text==texto_limpo:
    print("Passou")
else:
    print("Erro")
    



