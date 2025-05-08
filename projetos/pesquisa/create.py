import pandas as pd
import random
from faker import Faker
import re

fake = Faker('pt_BR')

# Gera 100 registros falsos
data = []
cores = ['Branca', 'Preta', 'Parda', 'Amarela', 'Indígena']
sexos = ['Masculino', 'Feminino']

for _ in range(100):
    nome = fake.name()
    endereco = fake.address().replace('\n', ', ')
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65).isoformat()
    cor = random.choice(cores)
    sexo = random.choice(sexos)
    identidade = fake.random_number(digits=8, fix_len=True)
    cpf = fake.cpf()

    # Tenta extrair o estado (sigla de 2 letras no final do endereço)
    estado_match = re.search(r'/\s*([A-Z]{2})$', endereco)
    estado = estado_match.group(1) if estado_match else "NA"

    data.append({
        'Nome': nome,
        'Endereço': endereco,
        'Estado': estado,
        'Data de nascimento': data_nascimento,
        'Cor': cor,
        'Sexo': sexo,
        'Identidade': f"{identidade:08d}-{random.randint(0,9)}",
        'CPF': cpf
    })

# Cria o DataFrame
df = pd.DataFrame(data)

# Salva como CSV
df.to_csv("lista_100_pessoas_com_estado.csv", index=False)
