# Abordagens Heurísticas para o Problema de Roteamento da Produção

Este repositório contém os códigos e experimentos desenvolvidos como parte do Trabalho de Conclusão de Curso **"Abordagens Heurísticas para o Problema de Roteamento da Produção"**.

## Sobre o projeto

O **Problema de Roteamento da Produção (Production Routing Problem – PRP)** é um problema de otimização combinatória que integra decisões de **produção, gerenciamento de estoques e roteamento de veículos** em um horizonte de planejamento com múltiplos períodos.

O objetivo deste projeto é investigar e implementar **abordagens heurísticas e estratégias de decomposição** capazes de obter soluções viáveis e de boa qualidade para o PRP, especialmente em instâncias de maior porte, nas quais a resolução exata pode apresentar elevado custo computacional.

O problema considera diferentes decisões interdependentes, incluindo:

* quantidade a ser produzida em cada período;
* níveis de estoque da planta;
* níveis de estoque dos clientes;
* atendimento da demanda ao longo do horizonte de planejamento;
* quantidade de produtos transportada para cada cliente;
* definição das rotas de distribuição;
* capacidade dos veículos;
* custos de produção, estoque e transporte.

## Abordagem

A estratégia desenvolvida explora a decomposição do problema em componentes relacionados ao **dimensionamento de lotes e estoque** e ao **roteamento de veículos**.

O algoritmo de **Wagner-Whitin**, baseado em programação dinâmica, é utilizado como apoio à determinação das decisões de produção e dimensionamento de lotes. A partir dessas decisões, são construídas e avaliadas soluções para o componente de distribuição e roteamento.

Para o desenvolvimento e avaliação dos modelos e heurísticas, são utilizadas ferramentas de **Programação Matemática e Otimização Combinatória**, incluindo:

* **Python** – linguagem utilizada na implementação dos modelos;
* **PyVRP** – ferramenta utilizada para apoiar a resolução do componente de roteamento;
* **Wagner-Whitin** – programação dinâmica aplicada ao dimensionamento de lotes.


## Objetivo

O projeto busca avaliar a capacidade das abordagens heurísticas de produzir soluções **viáveis, competitivas e computacionalmente eficientes**, considerando simultaneamente os custos e restrições associados à produção, estoque e transporte.

Os experimentos são realizados utilizando instâncias de referência do PRP, permitindo comparar diferentes estratégias de solução a partir de métricas como:

* custo total da solução;
* custo de produção;
* custo de estoque;
* custo de transporte;
* viabilidade das soluções;
* tempo computacional;
* qualidade das soluções obtidas.

## Contexto acadêmico

Este projeto foi desenvolvido no contexto de um Trabalho de Conclusão de Curso na área de **Ciência da Computação**, com foco em **Otimização Combinatória, Pesquisa Operacional, Heurísticas e Problemas de Roteamento**.
