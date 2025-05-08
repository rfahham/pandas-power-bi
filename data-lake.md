# Data Lake

Um **Data Lake** é um repositório centralizado que permite armazenar grandes volumes de dados em seu **formato bruto**, ou seja, sem a necessidade de estruturação prévia (como em bancos de dados tradicionais). Ele pode conter:

* Dados estruturados (como tabelas de bancos de dados),
* Dados semi-estruturados (como JSON, XML),
* Dados não estruturados (como vídeos, imagens, PDFs, áudios),
* Dados em tempo real ou históricos.

### Características principais de um Data Lake:

* **Escalabilidade**: Projetado para lidar com petabytes de dados.
* **Flexibilidade**: Armazena qualquer tipo de dado, sem necessidade de esquema pré-definido (esquema sob leitura, e não sob escrita).
* **Custo-benefício**: Normalmente usa armazenamento em nuvem, que é mais barato que soluções tradicionais de bancos de dados.
* **Integração com ferramentas de Big Data**: Como Apache Spark, Hadoop, ferramentas de machine learning, etc.

### Diferença entre Data Lake e Data Warehouse:

| Característica       | Data Lake                        | Data Warehouse                 |
| -------------------- | -------------------------------- | ------------------------------ |
| Tipo de dado         | Bruto (qualquer tipo)            | Estruturado (formatado)        |
| Flexibilidade        | Alta                             | Baixa                          |
| Custo                | Mais barato (armazenamento)      | Mais caro (processamento)      |
| Performance de query | Mais lenta (sem otimização)      | Alta (otimizado para consulta) |
| Usuários típicos     | Cientistas de dados, engenheiros | Analistas de negócios          |

Um exemplo famoso de Data Lake é o **Amazon S3**, que é amplamente usado para armazenar dados antes de serem processados por outras ferramentas.

