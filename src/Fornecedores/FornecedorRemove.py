from Fornecedores.FornecedorLista import DataProvider
from Verify.verification import validation
import sqlite3
def RemoveProvider():
    fornecedor_id = validation(int,"Qual o ID do fornecedor que irá ser excluído? ",False)
    #Envia o ID do fornecedor para a lista
    caminho = DataProvider("Remover",fornecedor_id = fornecedor_id)
    #Se o produto existir excluí o produto
    if caminho:
        certeza = input(f"\n Você tem certeza que quer excluir o fornecedor: {fornecedor_id}, (y/n): ")
        if certeza.lower() == "y":
                conexao = sqlite3.connect(caminho)
                cursor = conexao.cursor()
                cursor.execute("""
                            DELETE FROM FORNECEDORES
                               WHERE Fornecedor_ID = ?""", (fornecedor_id,))
                print(f"\nO fornecedor {fornecedor_id} foi removido")
                conexao.commit()
                cursor.close()
                conexao.close()
    else:
        print(f"\nNão foi possível achar o fornecedor com o ID {fornecedor_id}")
    