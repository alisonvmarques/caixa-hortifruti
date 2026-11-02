from decimal import Decimal

produto = input("Produto: ")

quantidade_texto = input("Quantidade: ")
quantidade = Decimal(quantidade_texto)

preco_texto = input("Preço: ")
preco = Decimal(preco_texto)

pagamento = input("Forma de Pagamento: ")

total = quantidade * preco

venda_grande = total > Decimal(50)
pagou_pix = pagamento == "pix"

print(f"A quantidade de {quantidade} X o preço de {preco} = ao total de {total}")
print(f"O total passou de 50: {venda_grande} e a forma de pagamento foi PIX: {pagou_pix}")
