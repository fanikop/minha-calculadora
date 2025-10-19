from calc import soma, subtracao, multiplicacao, divisao

def menu():
	print("=== Calculadora Simples ===)
	print("1.Soma)
	print("2.Subtracção)
	print("3.Mulltiplicação)
	print(4.Divisão)
	print("5.Sair)
	return input("Escolha uma opção (1-5): ")

def main():
	while True:
		opcao = Menu()
		if opcao == "5":
			print("Saindo...")
			break
		if opcao not in ["1", "2", "3", "4"]:
			print("Opção inváldia")
		try:
			a = float(input(Insira o primeiro número: "))
			b = float(input(Insira o segundo número: "))

			if opcao == "1"
				print(f"Resultado: {soma(a, b)}")
			elif opcao == "2"
				print(f"(Resultado: {subtracao(a, b)}")
			elif opcao == "3":
                		print(f"Resultado: {multiplicacao(a, b)}")
            		elif opcao == "4":
                		print(f"Resultado: {divisao(a, b)}")

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception:
            print("Erro inesperado!")


if __name__ == "__main__":
    main()
