#Desenvolva um programa que solicite ao usuário uma frase e imprima o número de caracteres, de palavras e de espaços em branco nesta frase.

def questao4():
    '''Inserção de dados, tratados os dados como numeros de caracteres, espaços em brancos e palavras.'''
    texto = input("Digite uma frase: ")
    
    contagem_caracteres = len(texto)
    
    contagem_branco = texto.count(" ")
    
    contagem_palavras = len(texto.split())
    
    print(f"O número de caracteres é: {contagem_caracteres}.")
    print(f"O número de espaços em brancos é: {contagem_branco}.")
    print(f"O número de palavras é: {contagem_palavras}")
    
questao4()