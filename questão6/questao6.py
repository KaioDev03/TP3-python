#Calcular o resultado de uma expressão matemática básica fornecida como string pelo usuário, ignorando espaços, permitindo apenas caracteres numéricos e os operadores +, -, * e /.
#Exemplo: '2 + 3 * 4' Resultado: 14.

def questao6():
    
    string_number = input("Digite uma expressão matemática: ")
    
    string_number = string_number.replace(" ", "")
    
    for char in string_number:
        if char not in "0123456789+-*/":
            print("Erro. A expressão está incorrenta. Tente novamente.")
            return
        
    try:
        resultado = eval(string_number)
        print(f"O resultado da expressão é: {resultado}")
        
    except Exception as e:
        print(f"Erro ao calcular a expressão: {e}")
        
questao6()