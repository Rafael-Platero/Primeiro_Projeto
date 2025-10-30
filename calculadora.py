while True:
    print("\nEscolha a operação que deseja calcular:")
    print("1 - ROI")
    print("2 - Lucro")
    print("3 - Margem")
    print("4 - Payback")
    print("5 - Sair")
    escolha = int(input("Escolha: "))
    
    if escolha == 5:
        print("Encerrando a calculadora, até logo!")
        break

    ganho = float(input("Ganho: "))
    custo = float(input("Custo: "))

    if escolha == 1:
        roi = ((ganho - custo) / custo) * 100
        print(f"O ROI é {roi:.2f}%")
    elif escolha == 2:
        lucro = ganho - custo
        print(f"O lucro é {lucro:.2f}")
    elif escolha == 3:
        if ganho != 0:
            margem = ((ganho - custo) / ganho) * 100
            print(f"A margem é {margem:.2f}%")
        else:
            print("Erro: ganho não pode ser zero")
    elif escolha == 4:
        lucro = ganho - custo
        if lucro > 0:
            payback = custo / lucro
            print(f"O Payback é {payback:.2f} períodos")
        else:
            print("Não é possível calcular Payback (não houve lucro)")
    else:
        print("Escolha inválida.")

    print("-" * 30)
