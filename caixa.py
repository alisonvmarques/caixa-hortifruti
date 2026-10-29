from decimal import Decimal

produto = input("Produto: ")

quantidade_texto = input("Quantidade: ")
quantidade = Decimal(quantidade_texto)

preco_texto = input("Preço: ")
preco = Decimal(preco_texto)

pagamento = input("Forma de Pagamento: ")

total = quantidade * preco

print(produto, type(produto))
print(quantidade, type(quantidade))
print(preco, type(preco))
print(pagamento, type(pagamento))
print(f"A quantidade de {quantidade} X o preço de {preco} = ao total de {total}")
