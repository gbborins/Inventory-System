import sqlite3
import csv

def exportar_vendas_csv():
    conn = sqlite3.connect("sistema.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            v.venda_id,
            v.data_venda,
            c.nome,
            p.nome,
            iv.quantidade,
            iv.preco_unitario,
            (iv.quantidade * iv.preco_unitario) as total
        FROM vendas v
        JOIN clientes c ON v.cliente_id = c.cliente_id
        JOIN itens_venda iv ON v.venda_id = iv.venda_id
        JOIN produtos p ON iv.produto_id = p.produto_id
    """)

    dados = cursor.fetchall()

    with open("relatorio_vendas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        
        writer.writerow([
            "venda_id", "data", "cliente", "produto",
            "quantidade", "preco_unitario", "total"
        ])
        
        writer.writerows(dados)

    conn.close()