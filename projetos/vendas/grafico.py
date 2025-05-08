# pip install pandas matplotlib seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do arquivo CSV
arquivo_csv = "vendas_filiais.csv"
df = pd.read_csv(arquivo_csv)

# Imprimir os dados
print("Dados de Vendas por Filial:")
print(df.head(20))  # mostra as 20 primeiras linhas

# Converter coluna "Mês" para datetime
df['Mês'] = pd.to_datetime(df['Mês'])

# Ordenar por data para garantir consistência
df = df.sort_values(by='Mês')

# ----- DASHBOARD -----

# Estilo do gráfico
sns.set(style="whitegrid")

# Gráfico 1: Vendas totais por mês (todas as filiais)
plt.figure(figsize=(12, 6))
df_grouped = df.groupby("Mês")["Total_Vendas"].sum().reset_index()
sns.lineplot(data=df_grouped, x="Mês", y="Total_Vendas", marker="o")
plt.title("Total de Vendas Mensais (Todas as Filiais)")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 2: Vendas por filial ao longo do tempo
plt.figure(figsize=(14, 8))
sns.lineplot(data=df, x="Mês", y="Total_Vendas", hue="Filial", marker="o")
plt.title("Vendas por Filial ao Longo dos Meses")
plt.xlabel("Mês")
plt.ylabel("Total de Vendas (R$)")
plt.legend(title='Filial', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Agrupamento necessário para o gráfico
df_filial_total = df.groupby("Filial")["Total_Vendas"].sum().reset_index()

# Gráfico 3: Total de vendas por filial (acumulado no ano)
plt.figure(figsize=(10, 6))
sns.barplot(data=df_filial_total, x="Filial", y="Total_Vendas", hue="Filial", palette="viridis", legend=False)
plt.title("Total de Vendas por Filial (Últimos 12 meses)")
plt.ylabel("Total de Vendas (R$)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
