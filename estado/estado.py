import pandas as pd
import plotly.express as px

# Lê o arquivo CSV
df = pd.read_csv("../lista_100_pessoas_com_estado.csv")

# Conta quantas pessoas há em cada estado
contagem_estados = df['Estado'].value_counts()

# Calcula o percentual
percentual_estados = df['Estado'].value_counts(normalize=True) * 100

# Junta as duas informações em um novo DataFrame
estatisticas_estados = pd.DataFrame({
    'Quantidade': contagem_estados,
    'Percentual (%)': percentual_estados.round(2)
})

# Salva os dados no arquivo CSV
estatisticas_estados.to_csv('estado.csv', index=True)

# Exibe o resultado
print(estatisticas_estados)

# Cria um gráfico interativo com Plotly
fig = px.bar(estatisticas_estados,
             x='Quantidade',
             y=estatisticas_estados.index,
             orientation='h',
             title='Distribuição por Estado',
             labels={'Quantidade': 'Quantidade de Pessoas', 'Estado': 'Estado'},
             text='Quantidade')

# Ajusta o texto dentro das barras
fig.update_traces(texttemplate='%{text}', textposition='inside')

# Exibe o gráfico
fig.show()
