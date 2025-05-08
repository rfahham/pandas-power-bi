import csv
from datetime import datetime, timedelta
import random

# Parâmetros
num_filiais = 10
meses = 12
arquivo_csv = "vendas_filiais.csv"

# Gerar os últimos 12 meses a partir do mês atual
hoje = datetime.today()
datas = [(hoje.replace(day=1) - timedelta(days=30 * i)).strftime("%Y-%m") for i in range(meses)]
datas.reverse()  # para ficar do mais antigo ao mais recente

# Criar e escrever no CSV
with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Filial", "Mês", "Total_Vendas"])

    for i in range(1, num_filiais + 1):
        for mes in datas:
            total_vendas = round(random.uniform(80000, 120000), 2)
            writer.writerow([f"Filial {i}", mes, total_vendas])

print(f"Arquivo '{arquivo_csv}' criado com sucesso.")
