Os níveis **Bronze**, **Prata** e **Ouro** representam uma **estratégia de camadas de dados** muito comum em arquiteturas de *Data Lake* e *Data Lakehouse*. Essa abordagem ajuda a organizar e padronizar o tratamento dos dados ao longo do seu ciclo de vida, da ingestão bruta até o consumo analítico.

---

### 🥉 **Bronze Layer (Dados Brutos - Raw)**

* **O que é**: Dados brutos, exatamente como vêm da fonte (sem transformação).
* **Exemplos**: Logs de sistemas, arquivos CSV, JSON de APIs, dumps de banco.
* **Objetivo**: Armazenamento rápido e íntegro de tudo que chega — usado para auditoria e rastreamento.
* **Formato comum**: JSON, CSV, Avro, Parquet.

📌 *Regra: Não se transforma nada aqui, apenas se copia ou organiza por data, partição, etc.*

---

### 🥈 **Prata Layer (Dados Limpos - Cleaned/Refined)**

* **O que é**: Dados limpos, normalizados e parcialmente transformados.
* **Transformações típicas**: Remoção de duplicatas, tratamento de valores nulos, padronização de colunas, joins simples.
* **Objetivo**: Tornar os dados confiáveis e utilizáveis por analistas e cientistas de dados.
* **Formato comum**: Parquet (otimizado para leitura), tabelas Delta.

📌 *Aqui os dados já têm mais estrutura e qualidade, mas ainda são genéricos — não modelados para um caso de negócio específico.*

---

### 🥇 **Ouro Layer (Dados Prontos para Negócio - Curated)**

* **O que é**: Dados prontos para análise e consumo por ferramentas BI, com lógica de negócio aplicada.
* **Exemplos**: Fatos e dimensões, indicadores de KPIs, dashboards.
* **Transformações típicas**: Cálculos de métricas, agregações, enriquecimento com dados externos.
* **Objetivo**: Consumir com confiança por usuários finais, dashboards, relatórios.
* **Formato comum**: Tabelas analíticas altamente otimizadas.

📌 *Esse é o “produto final” dos dados — geralmente usado diretamente por executivos, analistas e ferramentas como Power BI ou Looker.*

---

### 📊 Exemplo prático com dados de vendas:

| Nível  | Exemplo de Dado                                                           |
| ------ | ------------------------------------------------------------------------- |
| Bronze | JSON do sistema de pedidos brutos                                         |
| Prata  | Tabela limpa de pedidos, com joins com clientes e produtos                |
| Ouro   | Tabela com total de vendas por região, mês e canal, pronta para dashboard |

---

Essa estratégia também é conhecida como **"medallion architecture"**, muito utilizada em ferramentas como **Databricks**, **Delta Lake**, e outros ambientes de *Data Lakehouse*.

