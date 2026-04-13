# ♟️ Simulador de Movimentos de Xadrez (Python Edition)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

## 💻 Sobre o Projeto

Este projeto é uma refatoração em **Python** de um sistema de simulação de movimentos de xadrez originalmente escrito em C. O foco principal não é a interface gráfica do jogo, mas sim o estudo aprofundado de **Algoritmos de Navegação**, **Estruturas de Repetição Aninhadas** e **Recursividade**.

O sistema calcula e imprime no terminal a trajetória passo a passo de peças clássicas do xadrez, respeitando suas regras de deslocamento em um tabuleiro imaginário.

## ⚙️ Níveis de Complexidade e Implementação

O desenvolvimento foi segmentado em três níveis evolutivos de lógica de programação:

- **Nível Novato (Estruturas Básicas):** - Simulação do movimento da **Torre** (linha reta) e da **Rainha** (linha reta) utilizando loops simples (`for` ou `while`).

- **Nível Aventureiro (Loops Aninhados):** - Simulação do movimento do **Cavalo** (movimento em "L").
  - Aplicação de estruturas de repetição aninhadas para combinar movimentos verticais e horizontais em uma única jogada.

- **Nível Mestre (Recursividade e Controle de Fluxo):** - Substituição dos loops de peças lineares por **Funções Recursivas** (a função chamando a si mesma até atingir o caso-base).
  - Simulação do movimento complexo do **Bispo** e do **Cavalo** utilizando múltiplos loops aninhados combinados com cláusulas de controle de fluxo (`break` e `continue`).

## 🛠️ Tecnologias e Conceitos Aplicados

- **Linguagem:** Python 3.10+
- **Conceitos Chave:**
  - Recursividade (Call Stack e Casos-Base).
  - Controle de Fluxo Avançado (`while`, `for`, `break`, `continue`).
  - Lógica Algorítmica Estruturada.

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python instalado em sua máquina.

1. Clone este repositório:
   ```bash
   git clone [https://github.com/CRFjonathas/desafio-xadrez-python.git](https://github.com/CRFjonathas/desafio-xadrez-python.git)
