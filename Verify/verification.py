def validation(type ,text,menu = False):
    while True:
        #Exceção para verificar se está correto
        try:
            valor = type(input(text))
            #Exclusivo para menu
            if menu and (valor < 0 or valor > 10):
                print("\nDigite um valor válido")
                continue
        except ValueError:
            print("\nDigite um número válido")
        else:
            break
    #retorna o valor depois de conferir
    return valor