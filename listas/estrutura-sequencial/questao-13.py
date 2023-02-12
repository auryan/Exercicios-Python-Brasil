altura = float(input("Digite a sua altura: "))
sexo = input("Digite o seu sexo (H ou M): ")

if sexo == "H":
	print(f"O seu peso ideal é:{(72.7 * altura) - 58: .2f}")
elif sexo == "M":
	print(f"O seu peso ideal é:{(62.1 * altura) - 44.7: .2f}")
