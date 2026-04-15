from Clientes.ClienteLista import DataClient
from Verify.verification import validation
import sqlite3
def RemoveClient():
    cliente_id = validation(int,"Qual o ID do cliente que irá ser excluído? ",False)
    #Envia o ID do cliente para a lista
    caminho = DataClient("Remover",cliente_id = cliente_id)
    #Se o produto existir excluí o produto
    if caminho:
        certeza = input(f"\n Você tem certeza que quer excluir o cliente: {cliente_id}, (y/n): ")
        if certeza.lower() == "y":
                conexao = sqlite3.connect(caminho)
                cursor = conexao.cursor()
                cursor.execute("""
                            DELETE FROM CLIENTES
                               WHERE Cliente_ID = ?""", (cliente_id,))
                print(f"\nO cliente {cliente_id} foi removido")
                conexao.commit()
                cursor.close()
                conexao.close()
    else:
        print(f"\nNão foi possível achar o cliente com o ID {cliente_id}")
    