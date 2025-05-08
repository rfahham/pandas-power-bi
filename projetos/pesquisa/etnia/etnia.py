import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV
df = pd.read_csv("../lista_100_pessoas_com_estado.csv")

# Conta quantas pessoas há em cada grupo de cor
contagem_etnias = df['Cor'].value_counts()

# Calcula o percentual
percentual_etnias = df['Cor'].value_counts(normalize=True) * 100

# Junta as duas informações em um novo DataFrame
estatisticas_etnias = pd.DataFrame({
    'Quantidade': contagem_etnias,
    'Percentual (%)': percentual_etnias.round(2)
})

# Exibe o resultado
print(estatisticas_etnias)

# Salva os dados em um arquivo CSV
estatisticas_etnias.to_csv('etnia.csv', index=True)

# Cria gráfico de pizza
plt.figure(figsize=(8, 6))
plt.pie(estatisticas_etnias['Quantidade'], labels=estatisticas_etnias.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Distribuição por Etnia')
plt.axis('equal')  # Deixa o gráfico como um círculo
plt.tight_layout()
plt.show()
