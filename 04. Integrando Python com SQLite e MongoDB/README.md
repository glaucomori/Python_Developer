# Desafio - Integrando Python com SQLite e MongoDB

## Objetivo geral

- Aplicar os frameworks para integração do python a banco de dados.
- Definir a estrutura do banco de dados, criar instâncias e aplicar queries no banco de dados através de programação em python.

---

## Implementando um Banco de Dados Relacional com SQLAlchemy

Implementar uma aplicação de integração com SQLite com base em um esquema relacional disponibilizado nesse repositório. Utilizar o esquema dentro do contexto de cliente e conta para criar as classes de sua API. Essas classes irão representar as tabelas do banco de dados relacional dentro da aplicação.

Entregável:

- Aplicação com a definição do esquema por meio das classes usando SQLAlchemy
- Inserção de um conjunto de dados mínimo para manipulação das informações
- Execução de métodos de recuperação de dados via SQLAlchemy

---

## Implementando um Banco de Dados NoSQL com Pymongo

implementar um banco NoSQL com mongodb para fornecer uma visão agregada do modelo relacional. Sendo assim, as informações de cliente e contas existentes estão contidas dentro de documentos de acordo com cliente.

Executar as operações:

- Conecte ao mongo atlas e crie um banco de dados
- Defina uma coleção bank para criar os documetos de clientes
- Insira documentos com a estrutura mencionada
- Escreve instruções de recuperação de informações com base nos pares de chave e valor como feito em aula
