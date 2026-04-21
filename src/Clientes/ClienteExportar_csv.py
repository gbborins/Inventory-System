import sqlite3
import csv
from pathlib import Path
def Exportar_Cliente():
    path_db = Path(input("Digite o nome do arquivo DataBase: "))
    path_csv = Path(input("Digite o nome do arquivo csv: "))
    database_file = Path(__file__).resolve().parent.parent.parent / "database" / path_db
    csv_file = Path(__file__).resolve().parent.parent.parent / "data" / path_csv
    conect = sqlite3.connect(database_file)
    cursor = conect.cursor()
    cursor.execute("""
        SELECT 
            Cliente_ID,
            NomeCliente,
            CPF,
            Email,
            Telefone,
            Endereco FROM CLIENTES
    """)
    dados = cursor.fetchall()

    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not Path(csv_file).stat().st_size > 0:
            writer.writerow([
                "Cliente_ID", "NomeCliente","CPF",
                "Email","Telefone","Endereco"
            ])
            
        writer.writerows(dados)

    conect.close()