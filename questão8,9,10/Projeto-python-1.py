#Mini Projeto 1: Validação e Formatação de Dados em um Sistema de Cadastro

#Na vida de um desenvolvedor e analista de sistemas a validação de dados é uma etapa extremamente importante que previne diversas dificuldades posteriores à coleta dos dados.

#Crie um programa com funções em Python para solicitar ao usuário que insira os dados listados abaixo e valide os seguintes campos de cadastro com as seguintes regras:
#CPF: verifique se o CPF possui 11 dígitos e formate-o no padrão "xxx.xxx.xxx-xx".
#E-mail: verifique se o e-mail possui um formato válido (com "@" e um domínio válido) e normalize-o para minúsculas. Caracteres alfanuméricos + ‘@’ + Caracteres alfanuméricos + ‘.’ + Caracteres alfabéticos
#Telefone: remova caracteres não numéricos e converta o número de telefone para um número inteiro e em uma string formatada como (XX) XXXXX-XXXX ou (XX) XXXX-XXXX e exibindo o inteiro e a string formatada na tela.

import re

def validar_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = re.sub(r'\D', '', cpf)
    
    # Verifica se tem 11 dígitos
    if len(cpf) != 11:
        return False
    
    # Formata o CPF
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf_formatado

def validar_email(email):
    # Normaliza para minúsculas
    email = email.lower()
    
    # Expressão regular para validar o formato do e-mail
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        return email
    else:
        return None

def validar_telefone(telefone):
    # Remove caracteres não numéricos
    telefone = re.sub(r'\D', '', telefone)
    
    # Verifica o comprimento e formata o telefone
    if len(telefone) == 11:  # Para número de 11 dígitos
        telefone_formatado = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
        return telefone, telefone_formatado
    elif len(telefone) == 10:  # Para número de 10 dígitos
        telefone_formatado = f'({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}'
        return telefone, telefone_formatado
    else:
        return None, None

def main():
    # Solicita CPF
    cpf = input("Digite o seu CPF (sem pontos ou hífen): ")
    cpf_formatado = validar_cpf(cpf)
    if cpf_formatado:
        print(f"Seu CPF formatado é: {cpf_formatado}")
    else:
        print("O seu CPF é inválido. Deve conter 11 dígitos.")
    
    # Solicita e-mail
    email = input("Digite seu e-mail: ")
    email_normalizado = validar_email(email)
    if email_normalizado:
        print(f"Seu e-mail normalizado é: {email_normalizado}")
    else:
        print("O e-mail informado é inválido.")
    
    # Solicita telefone
    telefone = input("Digite seu telefone: ")
    telefone_inteiro, telefone_formatado = validar_telefone(telefone)
    if telefone_formatado:
        print(f"Seu telefone (inteiro) é: {telefone_inteiro}")
        print(f"Seu telefone formatado é: {telefone_formatado}")
    else:
        print("O telefone informado é inválido. Deve conter 10 ou 11 dígitos.")

if __name__ == "__main__":
    main()
