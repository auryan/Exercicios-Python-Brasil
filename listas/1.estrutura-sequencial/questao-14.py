print("Olá, João! Seja bem-vindo!", end="\n")

peso = float(input("Digite o peso do peixe: "))
excesso, multa = 0, 0

if peso > 50:
	excesso = peso - 50
	multa = excesso * 4
	print(f"\nValor do excesso:{excesso: .2f} Kg")
	print(f"Valor da multa: R${multa: .2f}")
else:
	print("\nNão houve excesso e nem multa :)")
