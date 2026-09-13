comum = 5.5
aditivada = 6.0
diesel = 4.5
etanol = 4.3

while True:
    switch = input("Digite o tipo de combustível: 1-Comum - R$5.5\n2-Aditivada - R$6.0\n3-Diesel - R$4.5\n4-Etanol - R$4.3\n")

    if switch == "1":
        litragem = float(input("Você selecionou o combustível Comum, digite a quantidade de litros: "))
        print(f"Você colocou {litragem} litros de combustível Comum. O valor total a ser pago é: R${litragem * comum:.2f}")
        break
    elif switch == "2":
        litragem = float(input("Você selecionou o combustível Aditivada, digite a quantidade de litros: "))
        print(f"Você colocou {litragem} litros de combustível Aditivada. O valor total a ser pago é: R${litragem * aditivada:.2f}")
        break
    elif switch == "3":
        litragem = float(input("Você selecionou o combustível Diesel, digite a quantidade de litros: "))
        print(f"Você colocou {litragem} litros de combustível Diesel. O valor total a ser pago é: R${litragem * diesel:.2f}")
        break
    elif switch == "4":
        litragem = float(input("Você selecionou o combustível Etanol, digite a quantidade de litros: "))
        print(f"Você colocou {litragem} litros de combustível Etanol. O valor total a ser pago é: R${litragem * etanol:.2f}")
        break
    else:
        print("Opção inválida. Tente novamente digitando uma opção válida.")