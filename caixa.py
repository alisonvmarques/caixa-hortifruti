from decimal import Decimal

produto = input("Produto: ")

quantidade_texto = input("Quantidade: ")
quantidade = float(quantidade_texto)

preco_texto = input("Preço: ")
preco = Decimal(preco_texto)

pagamento = input("Forma de Pagamento: ")

print(produto, type(produto))
print(quantidade, type(quantidade))
print(preco, type(preco))
print(pagamento, type(pagamento))
