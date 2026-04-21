#Fornecedores listados
import sqlite3
from pathlib import Path
def DataProvider(funcao,nome_empresa = None,cnpj = None,email = None,
                telefone = None,endereco = None,fornecedor_id = None,produto_id = None,
                quant = None,preco = None, data_compra = None):
    path = Path(input("Digite o nome do arquivo DataBase: "))
    database_file = Path(__file__).resolve().parent.parent.parent / "database" / path
    conexao = sqlite3.connect(database_file)
    cursor = conexao.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS FORNECEDORES(
                    Fornecedor_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NomeEmpresa TEXT,
                    CNPJ TEXT,
                    Email TEXT,
                    Telefone TEXT,
                    Endereco TEXT
                    );""")
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS FORNECEDORES_COMPRA(
                    Compra_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Fornecedor_ID INTEGER ,
                    Produto_ID INTEGER,     
                    Quantidade INTEGER,
                    Preco FLOAT,
                    Data_Compra DATE,
                    Valor_Total_Compra FLOAT
                    );""")
    if funcao == "Cadastro":
        Achou = False
        #Seleciona todas as linhas com o nome_empresa do Fornecedores
        cursor.execute("SELECT * FROM FORNECEDORES WHERE NomeEmpresa = ?",(nome_empresa,))
        while True:
            #Coleta linha por linha da database
            resultado = cursor.fetchone()
            if resultado is None:
                #Caso seja vazia ou chegado ao fim da tabela
                break
            elif resultado[1] == nome_empresa:
                #Se o fornecedor foi encontrado
                Achou = True
                break
        #Caso não seja achado o fornecedor
        if not Achou:
            #Escreve no arquivo database
            cursor.execute("""
                        INSERT INTO FORNECEDORES (NomeEmpresa, CNPJ, Email, Telefone, Endereco)
                           VALUES (?,?,?,?,?)
                            """, (nome_empresa, cnpj, email, telefone, endereco))
            fornecedor_id_ID = cursor.lastrowid
            print(f"\nO fornecedor {fornecedor_id_ID} cadastrado com sucesso")
        else:
            subs = input("O fornecedor foi achado, desejs substituir os dados (y/n)")
            if subs.lower() == "y":
                cursor.execute("""
                            UPDATE FORNECEDORES
                               SET CNPJ = ?, Email = ?, Telefone = ?, Endereco = ?
                               WHERE NomeEmpresa = ?""",(cnpj,email,telefone,endereco,nome_empresa))
                print("\nOs valores foram alterados com sucesso")
    elif funcao == "Buscar":
        decisao = input("Está buscando um fornecedor (1) ou uma compra de fornecedor (2)? ")
        if decisao == "1":
            #Verifica se o fornecedor_id está em alguma linha
            if fornecedor_id:
                cursor.execute("SELECT * FROM FORNECEDORES WHERE Fornecedor_ID = ?", (fornecedor_id,))
            resultado = cursor.fetchone()
            if resultado:
                return [
                    resultado[0],resultado[1],resultado[2],
                    resultado[3],resultado[4],resultado[5]]
            else:
                return False
    elif funcao == "Lista":
        decisao = input("A lista de um fornecedor (1) ou uma compra de fornecedor (2)? ")
        if decisao == "1":
            cursor.execute("SELECT * FROM FORNECEDORES")
            resultado = cursor.fetchall()
            for registro in resultado:
                print(f"""\nFornecedor_ID: {registro[0]} | NomeEmpresa: {registro[1]} | CNPJ: {registro[2]} 
                    | Email: {registro[3]} | Telefone: {registro[4]} | Endereco: {registro[5]}""")
    elif funcao == "Remover":
        decisao = input("Remover um fornecedor (1) ou uma compra de fornecedor (2)? ")
        if decisao == "1":
            cursor.execute("SELECT * FROM FORNECEDORES WHERE Fornecedor_ID = ?", (fornecedor_id,))
            resultado = cursor.fetchone()
            if resultado:
                return database_file
            else:
                return False
    elif funcao == "Compra":
        valorTotal = preco*quant
        cursor.execute("""
                INSERT INTO FORNECEDORES_COMPRA (
                    Fornecedor_ID,Produto_ID,Quantidade,
                    Preco,Data_Compra,Valor_Total_Compra)
                           VALUES (?,?,?,?,?,?)
                            """, (fornecedor_id, produto_id, quant, preco, data_compra,valorTotal))
        Compra_ID = cursor.lastrowid
        print(f"\nA compra {Compra_ID} cadastrado com sucesso")
    #Salva o arquivo para não perder as modificações
    conexao.commit()
    cursor.close()
    conexao.close()