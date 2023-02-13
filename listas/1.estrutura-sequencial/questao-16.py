tamanho = float(input("Digite o tamanho (em metros quadrados) da área a ser pintada: "))

# Se 1 litro de tinta pinta 3 metros quadrados, então:

if (tamanho % 3) != 0:
	litros = int((tamanho // 3) + 1)
else:
	litros = int(tamanho / 3)

# Se 1 lata de tinta contém 18 litros, então:

if (litros % 18) != 0:
	latas = int((litros // 18) + 1)
else:
	latas = int(litros / 18)

preco_lata = latas * 80

if latas > 1:
	print(f"Será necessário {latas} latas de tinta, custando no total R${preco_lata: .2f}")
else:
	print(f"Será necessário 1 lata de tinta, custando no total R${preco_lata: .2f}")
