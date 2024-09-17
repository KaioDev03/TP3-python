#Implemente uma função que receba uma string representando uma data no formato "dd/mm/aaaa" e retorne a data em um formato textual, por exemplo, "25/12/2024" -> "Vinte e cinco de dezembro de dois mil e vinte e quatro".

def questao8():
    dias = {
        "01": "Primeiro", "02": "Dois", "03": "Três", "04": "Quatro", "05": "Cinco", 
        "06": "Seis", "07": "Sete", "08": "Oito", "09": "Nove", "10": "Dez", 
        "11": "Onze", "12": "Doze", "13": "Treze", "14": "Quatorze", "15": "Quinze", 
        "16": "Dezesseis", "17": "Dezessete", "18": "Dezoito", "19": "Dezenove", "20": "Vinte", 
        "21": "Vinte e um", "22": "Vinte e dois", "23": "Vinte e três", "24": "Vinte e quatro", 
        "25": "Vinte e cinco", "26": "Vinte e seis", "27": "Vinte e sete", "28": "Vinte e oito", 
        "29": "Vinte e nove", "30": "Trinta", "31": "Trinta e um"
    }

    meses = {
        "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril", 
        "05": "maio", "06": "junho", "07": "julho", "08": "agosto", 
        "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
    }

    anos = {
        "2000": "dois mil",
        "2001": "dois mil e um", "2002": "dois mil e dois", "2003": "dois mil e três", 
        "2004": "dois mil e quatro", "2005": "dois mil e cinco", "2006": "dois mil e seis", 
        "2007": "dois mil e sete", "2008": "dois mil e oito", "2009": "dois mil e nove", 
        "2010": "dois mil e dez", "2011": "dois mil e onze", "2012": "dois mil e doze", 
        "2013": "dois mil e treze", "2014": "dois mil e quatorze", "2015": "dois mil e quinze", 
        "2016": "dois mil e dezesseis", "2017": "dois mil e dezessete", "2018": "dois mil e dezoito", 
        "2019": "dois mil e dezenove", "2020": "dois mil e vinte", "2021": "dois mil e vinte e um", 
        "2022": "dois mil e vinte e dois", "2023": "dois mil e vinte e três", "2024": "dois mil e vinte e quatro"
    }

    data = input("Digite a data no formato dd/mm/aaaa: (Apenas de 2000 até 2024)")
    
    dia, mes, ano = data.split("/")
    
    dia_texto = dias.get(dia, "Dia inválido")
    mes_texto = meses.get(mes, "Mês inválido")
    ano_texto = anos.get(ano, "Ano inválido")

    return f"{dia_texto} de {mes_texto} de {ano_texto}"

resultado = questao8()
print(resultado)