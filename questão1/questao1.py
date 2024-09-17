# Crie um programa que solicite um nome completo ao usuário e formate-o de forma que todas as palavras comecem com letra maiúscula e o restante seja #minúsculo e exiba-o na tela.

def questao1():
    '''Loop criado para tratar os dados, se houver numeros em vez de letras, da erro. 
    Se houver letras maiusculas, é tratado para todas serem minusculas(lower()).
    E tratadas novamente para atender a demanda do programa usando o (isalpha()).
    Usado o replace para ler apenas a strings e excluir os espaços em brancos para evitar outro problema do programa.
    '''
    while True:
        
        nome_completo = input("Digite seu nome completo: ")
        
        if nome_completo.replace(" ", "").isalpha():
            
            nome_completo_tratado = nome_completo.lower().title()
            print(f"Texto formatado: {nome_completo_tratado}")
            break
        
        else:
            print(f"A entrada contém números. Digite apenas letras.")
            
questao1()