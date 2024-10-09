# Projeto de Automação com Python

Este projeto foi desenvolvido como parte da Jornada Python, com o objetivo de automatizar o cadastro de produtos em um sistema, utilizando a biblioteca PyAutoGUI para controlar o mouse e o teclado. Com isso, eliminamos a necessidade de realizar cadastros manuais repetitivos.

## Objetivo do Projeto

O projeto visa automatizar o processo de cadastro de produtos em um sistema online, lendo os dados de uma base em formato CSV e utilizando Python para replicar as ações de um usuário humano, como preencher campos e submeter formulários.

## Funcionalidades

- **Automação de Login**: O programa realiza login automático no sistema usando PyAutoGUI para preencher o usuário e senha e clicar no botão de login.
- **Cadastro de Produtos**: A cada iteração, o script percorre as linhas da base de dados, preenchendo os campos de produto no sistema de forma automatizada.
- **Verificação Condicional**: O script verifica se há informações adicionais no campo de observação antes de submetê-las.
- **Economia de Tempo**: Automatiza o cadastro de centenas de produtos, poupando tempo e minimizando a margem de erro humano.

## Tecnologias Utilizadas

- **Python**
- **PyAutoGUI**: Para automação de ações no sistema (controlar mouse, teclado e cliques).
- **Pandas**: Para manipulação e leitura da base de dados no formato CSV.

## Estrutura do Projeto
- **codigo.py**: Script principal que realiza a automação.
- **p.csv**: Base de dados dos produtos a serem cadastrados.
- **auxiliar.py**: Script auxiliar para capturar as coordenadas do mouse.

## Conclusão
Este projeto demonstra como podemos automatizar tarefas repetitivas, como o cadastro de produtos em sistemas, utilizando o Python e a biblioteca PyAutoGUI. A automação não só economiza tempo, como também reduz a probabilidade de erros.

