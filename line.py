last = int(input(f"quantidade inicial"))
line = list(range(1,last+1))
while True:
    print(f"{len(line)} clientes restantes")
    print(f"fila atual: {line}")
    choice = str(input("Digite C(adicionar cliente), A(atendimento), F(fechar)"))
    if choice.lower() == "a":
        if len(line) > 0:
            aten = line.pop(0)
            print(f"Cliente {aten} atendido"}
        else:
            print(f"Não há ninguém")
    elif choice.lower() == "c":
        ultimo += 1
        fila.append(ultimo)
    elif choice.lower() == "f":
        break
    else:
        print("Operacao inválida")