#Escreva uma função que receba um texto e retorne a palavra mais longa presente nele, desconsiderando pontuação.

def questao3():
    '''Função criada para chamar a função 'frase' a entrada do usuário e encontrar a palavra mais longa.'''
    def frase():
        '''Captura a entrada dos dados, tratamento para evitar fins de erro no programa.
        Dividimos o texto em palavras dentro de uma lista e é feito uma iteração para percorrer todas as palavras e descobrir qual a maior e imprimir.'''
        texto = input("Digite aqui o que quiser: ")
        
        texto_tratado = texto_tratado = texto.replace(',', '').replace('.', '').replace(';', '').replace('!', '').replace('?', '')
        
        texto_tratado = texto_tratado.split()
        
        palavra_longa = ""
        comprimento_maximo = 0
        
        for palavra in texto_tratado:
            if len(palavra) > comprimento_maximo:
                palavra_longa = palavra
                comprimento_maximo = len(palavra)
                
        print(f"A palavra mais longa é: {palavra_longa}")
        
    frase()
    
questao3()