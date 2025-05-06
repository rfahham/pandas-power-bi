import pandas as pd
from datetime import datetime
import plotly.express as px

# Lê o arquivo CSV
df = pd.read_csv("../lista_100_pessoas_com_estado.csv")

# Converte a coluna 'Data de nascimento' para o tipo datetime
df['Data de nascimento'] = pd.to_datetime(df['Data de nascimento'])

# Calcula a idade com base na data de nascimento
df['Idade'] = (datetime.now() - df['Data de nascimento']).dt.days // 365

# Definindo as faixas etárias
bins = [0, 18, 25, 35, 45, 60, 100]
labels = ['0-18', '19-25', '26-35', '36-45', '46-60', '60+']

# Cria a coluna 'Faixa Etária'
df['Faixa Etária'] = pd.cut(df['Idade'], bins=bins, labels=labels, right=False)

# Conta quantas pessoas há em cada faixa etária
contagem_faixa_etaria = df['Faixa Etária'].value_counts()

# Calcula o percentual
percentual_faixa_etaria = df['Faixa Etária'].value_counts(normalize=True) * 100

# Junta as duas informações em um novo DataFrame
estatisticas_faixa_etaria = pd.DataFrame({
    'Quantidade': contagem_faixa_etaria,
    'Percentual (%)': percentual_faixa_etaria.round(2)
})

# Inverte a ordem das faixas etárias para começar pelo mais novo
estatisticas_faixa_etaria = estatisticas_faixa_etaria.reindex(labels)

# Salva os dados em um arquivo CSV
estatisticas_faixa_etaria.to_csv('idade.csv', index=True)

# Exibe as estatísticas
print(estatisticas_faixa_etaria)

# Cria gráfico interativo
fig = px.bar(estatisticas_faixa_etaria,
             x=estatisticas_faixa_etaria.index,
             y='Quantidade',
             title='Distribuição de Faixa Etária',
             labels={'Quantidade': 'Quantidade de Pessoas', 'Faixa Etária': 'Faixa Etária'},
             text='Quantidade')

fig.update_traces(texttemplate='%{text}', textposition='outside')
fig.show()
