import pandas as pd
import plotly.express as px

# Lê o arquivo CSV
df = pd.read_csv("../lista_100_pessoas_com_estado.csv")

# Conta quantas pessoas há de cada sexo
contagem_sexo = df['Sexo'].value_counts()

# Calcula o percentual
percentual_sexo = df['Sexo'].value_counts(normalize=True) * 100

# Junta as duas informações em um novo DataFrame
estatisticas_sexo = pd.DataFrame({
    'Quantidade': contagem_sexo,
    'Percentual (%)': percentual_sexo.round(2)
})

# Exibe o resultado
print(estatisticas_sexo)

# Salva o DataFrame no arquivo CSV
estatisticas_sexo.to_csv('sexo.csv', index=True)

# Cria um gráfico interativo com Plotly
fig = px.bar(estatisticas_sexo,
             x=estatisticas_sexo.index,
             y='Quantidade',
             title='Distribuição por Sexo',
             labels={'Quantidade': 'Quantidade de Pessoas', 'Sexo': 'Sexo'},
             text='Quantidade')  # Exibe o número em cima de cada barra

# Exibe o gráfico interativo
fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.show()
