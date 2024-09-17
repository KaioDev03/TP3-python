#Uma empresa de comércio eletrônico deseja analisar os dados de vendas para entender melhor o comportamento dos clientes e otimizar as estratégias de marketing.

#Implemente um programa em Python que receba uma lista de transações, onde cada transação é representada por uma string no formato "ID_do_Produto,Nome_do_Produto,Quantidade,Valor_Unitário". O programa deve calcular e exibir o valor total das vendas para cada produto.
#Crie uma função que receba a lista de transações e retorne o produto mais vendido (baseado na quantidade) e o produto que gerou a maior receita total.
#Escreva um script que converta os valores totais de vendas para uma nova moeda, dado um fator de conversão fornecido pelo usuário. Exiba os valores convertidos no formato monetário adequado.

def calcular_valor_total_vendas(transacoes):
    vendas = {}
    
    for transacao in transacoes:
        nome_produto, quantidade, valor_unitario = transacao.split(',')[1:]
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario
        
        if nome_produto in vendas:
            vendas[nome_produto] += valor_total
        else:
            vendas[nome_produto] = valor_total
            
    return vendas

def analisar_vendas(transacoes):
    quantidade_vendida = {}
    receita_total = {}
    
    for transacao in transacoes:
        nome_produto, quantidade, valor_unitario = transacao.split(',')[1:]
        quantidade = int(quantidade)
        valor_unitario = float(valor_unitario)
        valor_total = quantidade * valor_unitario
        
        if nome_produto in quantidade_vendida:
            quantidade_vendida[nome_produto] += quantidade
            receita_total[nome_produto] += valor_total
        else:
            quantidade_vendida[nome_produto] = quantidade
            receita_total[nome_produto] = valor_total
            
    produto_mais_vendido = max(quantidade_vendida, key=quantidade_vendida.get)
    produto_maior_receita = max(receita_total, key=receita_total.get)
    
    return produto_mais_vendido, produto_maior_receita

def converter_moeda(vendas, fator_conversao):
    vendas_convertidas = {produto: valor * fator_conversao for produto, valor in vendas.items()}
    return vendas_convertidas

def main():
    # Lista de transações
    transacoes = [
        "001,ProdutoA,10,15.50",
        "002,ProdutoB,5,25.00",
        "003,ProdutoA,2,15.50",
        "004,ProdutoC,7,30.00",
        "005,ProdutoB,3,25.00",
    ]
    
    # Calcula o valor total das vendas para cada produto
    vendas = calcular_valor_total_vendas(transacoes)
    print("Valor total das vendas por produto:")
    for produto, valor in vendas.items():
        print(f"{produto}: R${valor:.2f}")
    
    # Analisa as vendas
    produto_mais_vendido, produto_maior_receita = analisar_vendas(transacoes)
    print(f"\nProduto mais vendido: {produto_mais_vendido}")
    print(f"Produto com maior receita: {produto_maior_receita}")
    
    # Converte valores para uma nova moeda
    try:
        fator_conversao = float(input("\nDigite o fator de conversão para a nova moeda: "))
        vendas_convertidas = converter_moeda(vendas, fator_conversao)
        print("\nValores convertidos para a nova moeda:")
        for produto, valor in vendas_convertidas.items():
            print(f"{produto}: {valor:.2f} (na nova moeda)")
    except ValueError:
        print("Valor de fator de conversão inválido.")

if __name__ == "__main__":
    main()
