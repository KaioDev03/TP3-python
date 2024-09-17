#Crie um script em Python que substitua todas as ocorrências de uma palavra específica em uma frase por outra palavra fornecida pelo usuário. Utilize um texto de exemplo de sua preferência e escolha a palavra a ser substituída, mas a lógica precisa funcionar para outros casos.

def questao2():
    '''Recebendo os dados e fazendo o tratamento deles.
    Frase inicial, qual palavra vai ser modificada na frase e escolhendo qual a palavra para mudar a frase.
    Uma condicional para saber se o usuário quer continuar a rodar o programa ou não.'''
    while True:
            
        entrada_frase = input("Digite uma frase: ")
        modifica_frase = input("Digite a palavra para substituir: ")
        palavra_nova = input("Digite uma nova palavra: ")
        
        frase_final = entrada_frase.replace(modifica_frase,palavra_nova)
        
        print(f"Frase modificada: {frase_final}")
        
        continuar = input("Você quer continuar? (sim/não): ").strip().lower()
    
        if continuar != 'sim':
            break
questao2()