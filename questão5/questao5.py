#Calcular a soma dos dígitos em uma string numérica fornecida pelo usuário, verificando se todos os caracteres são de fato numéricos.
#Exemplo: “123” Resultado: 1+2+3 = 6

def questao5():
    '''Inserção dos dados, estrutura condicional para tratar os dados apenas digitos númericos e mostrar o resultado.'''
    string_numerica = input("Digite uma string numerica: (exemplo: 56789)")
    
    if string_numerica.isdigit():
        
        soma = sum(int(digito)for digito in string_numerica)
        
        print(f"A soma dos digitos é: {soma}")
        
    else:
        print(f"Houve um erro, por favor digite apenas números.")
        
questao5()