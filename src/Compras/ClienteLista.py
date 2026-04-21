#Fornecedores listados
import sqlite3
from pathlib import Path
def DataClient(funcao,nome = None, Cpf = None,
                email = None, telefone = None, endereco = None,cliente_id = None):
    path = Path(input("Digite o nome do arquivo DataBase: "))
    database_file = Path(__file__).resolve().parent.parent.parent / "database" / path
    print(database_file)
    conexao = sqlite3.connect(database_file)
    cursor = conexao.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS CLIENTES(
                    Cliente_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Nome TEXT,
                    CPF TEXT,
                    Email TEXT,
                    Telefone TEXT,
                    Endereco TEXT
                    );""")
    if funcao == "Cadastro":
        Achou = False
        #Seleciona todas as linhas com o nome do cliente
        cursor.execute("SELECT * FROM CLIENTES WHERE Nome = ?",(nome,))
        while True:
            #Coleta linha por linha da database
            resultado = cursor.fetchone()
            if resultado is None:
                #Caso seja vazia ou chegado ao fim da tabela
                break
            if resultado[1] == nome:
                #Se o cliente foi encontrado
                Achou = True
                break
        #Caso não seja achado o cliente
        if not Achou:
            #Escreve no arquivo database
            cursor.execute("""
                        INSERT INTO CLIENTES (Nome, CPF, Email, Telefone, Endereco)
                           VALUES (?,?,?,?,?)
                            """, (nome, Cpf, email, telefone, endereco))
            cursor.execute("SELECT * FROM CLIENTES WHERE Nome = ?",(nome,))
            resultado = cursor.fetchone()
            print(f"\nCliente {resultado[0]} cadastrado com sucesso")
        else:
            subs = input("O cliente foi achado, desejs substituir os dados (y/n)")
            if subs.lower() == "y":
                cursor.execute("""
                            UPDATE CLIENTE
                               SET CPF = ?, Email = ?, Telefone = ?, Endereco = ?
                               WHERE nome = ?""",(Cpf,email,telefone,endereco,nome))
                print("\nOs valores foram alterados com sucesso")
    elif funcao == "Buscar":
        #Verifica se o cliente_id está em alguma linha
        if cliente_id:
            cursor.execute("SELECT * FROM CLIENTES WHERE Cliente_ID = ?", (cliente_id,))
        resultado = cursor.fetchone()
        if resultado:
            return [
                resultado[0],resultado[1],resultado[2],
                resultado[3],resultado[4],resultado[5]]
        else:
            return False
    elif funcao == "Lista":
        cursor.execute("SELECT * FROM CLIENTES")
        resultado = cursor.fetchall()
        for registro in resultado:
            print(f"""\nID: {registro[0]} | Nome: {registro[1]} | CPF: {registro[2]} 
                  | Email: {registro[3]} | Telefone: {registro[4]} | Endereco {registro[5]}""")
    elif funcao == "Remover":
        cursor.execute("SELECT * FROM CLIENTES WHERE Cliente_ID = ?", (cliente_id,))
        resultado = cursor.fetchone()

        if resultado:
            return database_file
        else:
            return False
    #Salva o arquivo para não perder as modificações
    conexao.commit()
    cursor.close()
    conexao.close()