def adicao (y, x):
    return y + x

print("selecione uma opção: ")
print("1.adição: ")
print("2.subtração: ")
print("3.multiplacação: ")
print("4.divisão: ")


opcao = int(input("escolha um aopção 1/2/3/4: "))

num1 = float(input("digite 1 numero: "))
num2 = float(input("digite 2 numero: "))

if opcao == 1:
    print(f"resultado: {adicao(num1 + num2)}")
elif opcao == 2:
    print(f"resultado: {num1}")
elif opcao == 3:
    print(f"resultado: {num1}")
elif opcao == 4:
    print(f"resultado: {num1}")
else:
    print(f"opção invalida")