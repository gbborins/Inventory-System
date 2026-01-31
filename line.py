while True:
    try:
        last = int(input(f"Quantidade inicial de clientes: "))
    except (ValueError, TypeError) as er:
        print("Por favor digite um número inteiro")
        continue
    line = list(range(1,last+1))
    break
while True:
    ultimo = line[-1] if len(line) > 0 else 0
    print(f"{len(line)} clientes restantes")
    print(f"fila atual: {line}")
    choice = str(input("Digite C(adicionar cliente), A(atendimento), F(fechar)"))
    if choice.lower() == "a":
        print(f"Cliente {line.pop(0)} atendido") if len(line) > 0 else print(f"Não há ninguém")
    elif choice.lower() == "c":
        line.append(ultimo + 1)
    elif choice.lower() == "f":
        break
    else:
        print("Operacao inválida")