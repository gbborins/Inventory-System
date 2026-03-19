import pandas as pd
def Estoque(nome,valor, quantidade):
    #Lê um arquivo excel
    df = pd.read_excel(r"D:\Programacao\Python\Proj2\Estoque\Items.xlsx")
        #Verifica se já está no estoque
    if nome not in df["Nome"].values:
        #Adiciona uma nova linha com os valores
        df.loc[len(df)] = [nome,valor,quantidade]
    else:
        linha = df[df["Nome"] == nome].index[0]
        #Substitui o novo valor
        if df.loc[linha,"Valor"] != valor:
            print("O valor mudou")
            df.loc[linha,"Valor"] = valor
            #Soma a quantidade com a já guardada
        df.loc[linha,"Quantidade"] += quantidade
        print(f"Houve um aumento de {quantidade} no produto {nome}")
    #Salva o arquivo para não perder as modificações
    df.to_excel(r"D:\Programacao\Python\Proj2\Estoque\Items.xlsx", index=False)