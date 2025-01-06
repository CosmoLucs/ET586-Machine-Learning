# Projeto de Estatística e Probabilidade

Este repositório contém o projeto de estatítica desenvolvido como parte da disciplina **ET586 - Estatítica e Probabilidade** do curso de Engenharia da Computação. O objetivo deste projeto é criar um modelo de aprendizado de máquina que seja capaz de classificar dados presente em um bando de dados escolhido pela equipe utilizando o nosso aprendizado sobre o **classificador ingênuo de Bayes**.

## Estrutura do Projeto

O projeto está dividido em **três** partes principais, cada uma correspondendo a um aspecto essencial do projeto:

### 1. Código
Nesta etapa, desenvolvemos o **código em python** do projeto, seu funcionamento, de forma resumida:
- **Pré-processamento dos dados**.
- **Implementação do modelo Naive Bayes**.
- **Validação e avaliação do modelo**.

O código foi construido utilizando as bibliotecas utilizadas nesse README e está disponível na pasta `src/`.

### 2. Dados 
Com base no banco de dados escolhido pela equipe, analisamos as **informações** relevantes para o nosso projeto da seguinte forma:
- **Limpeza e preparação dos dados.**
- **Análise exploratória dos dados (EDA).**
- **Divisão dos dados em treinamento e teste.**

O arquivos relacionados as informações de entrada e dados releveantes podem ser encontrado na pasta `data/`.

### 3. Apresetação e Relatórios
Após o desenvolvimento do projeto, produzimos os materiais para apresentação e documentação:
**Relatório do Projeto:** Detalha os métodos, resultados e conclusões.
**Slides de Apresentação:** Resumo visual do projeto para apresentação.

Os arquivos estão disponíveis na pasta `docs/`.

### Bibliotecas Utilizadas
-
-
-

O uso das bibliotecas pode ser visto dentro dos arquivos presentes na pasta `src/`. 

## Referências
- Clone este repositório:
   ```bash
   git clone https://github.com/CosmoLucs/ET586-Machine-Learning.git
- Banco de Dados utilizado: 

# Guidelines de Contribuição

## Mensagens de Commit

Utilizamos uma convenção que fornece um conjunto de regras para formular uma estrutura de mensagem de commit consistente da seguinte forma:

```
<type>[optional scope]: <description>
```

O tipo do commit pode ser:

- `feat` – uma nova funcionalidade é introduzida com as mudanças.
- `fix` – ocorreu uma correção de bug.
- `refactor` – código refatorado que não corrige um bug nem adiciona uma funcionalidade.
- `docs` – atualizações na documentação, como o README ou outros arquivos markdown.
- `style` – mudanças que não afetam o significado do código, provavelmente relacionadas à formatação do código, como espaços em branco, pontos e vírgulas ausentes, e assim por diante.

A linha de assunto do tipo de commit deve ser toda em letras minúsculas.

## Criação de Branches

Uma branch do git deve começar com uma categoria. Escolha uma destas: `feature`, `bugfix`, ou `test`.

- `feature` é para adicionar, refatorar ou remover uma funcionalidade.
- `bugfix` é para corrigir um bug.
- `test` é para experimentação.

Após a categoria, deve haver um "/" seguido por uma descrição que resume o propósito desta branch específica. Esta descrição deve ser curta e em `kebab-case`. Para resumir, siga este padrão ao criar branches:

```
git branch <category/description-in-kebab-case>
```

Exemplos:

- Você precisa adicionar, refatorar ou remover uma funcionalidade: `git branch feature/new-attempt`
- Você precisa corrigir um bug: `git branch bugfix/reading-problem`
- Você precisa experimentar algo: `git branch test/another-library`