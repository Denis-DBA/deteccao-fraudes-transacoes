# 📄 Relatório do Projeto

## 📌 Visão Geral

Este projeto tem como objetivo desenvolver um modelo de Machine Learning capaz de identificar transações fraudulentas com cartão de crédito. Para isso, foi utilizada uma base de dados previamente tratada contendo transações classificadas como fraudulentas ou não fraudulentas.

Durante o desenvolvimento foram realizadas etapas de exploração dos dados, pré-processamento, divisão entre treino e teste, treinamento do modelo e avaliação por meio de métricas de classificação.

---

# 📊 Dataset

O projeto utiliza o conjunto de dados **Credit Card Fraud Detection**, composto por transações realizadas com cartões de crédito.

Principais características:

- Variáveis anonimizadas (V1 até V28)
- Variável **Time**
- Variável **Amount**
- Variável alvo **Class**
  - **0:** Transação legítima
  - **1:** Transação fraudulenta

O conjunto apresenta forte desbalanceamento entre as classes, característica comum em problemas de detecção de fraudes.

---

# 🧹 Pré-processamento

As principais etapas realizadas foram:

- Carregamento da base de dados
- Verificação de valores ausentes
- Análise da distribuição das classes
- Separação das variáveis independentes e da variável alvo
- Divisão entre conjunto de treinamento e teste
- Padronização dos dados utilizando **StandardScaler**

---

# 🤖 Modelo Utilizado

Foi utilizado o algoritmo:

- Logistic Regression

O modelo foi organizado utilizando um **Pipeline** do Scikit-Learn, permitindo aplicar automaticamente a padronização dos dados e o treinamento do modelo em um único fluxo.

---

# 📈 Avaliação

O desempenho do modelo foi avaliado utilizando as seguintes métricas:

- Accuracy
- Precision
- Recall
- F1-score
- Matriz de Confusão

Essas métricas permitem analisar a capacidade do modelo em identificar corretamente transações fraudulentas e minimizar erros de classificação.

---

# 📌 Resultados

O modelo apresentou bom desempenho na identificação das classes, sendo capaz de distinguir transações legítimas de fraudulentas utilizando técnicas de classificação supervisionada.

Como o conjunto de dados é altamente desbalanceado, métricas como **Precision**, **Recall** e **F1-score** foram consideradas mais representativas do desempenho do modelo do que apenas a acurácia.

---

# 🎯 Conclusão

Este projeto permitiu aplicar na prática conceitos fundamentais de Ciência de Dados e Machine Learning, incluindo:

- Análise exploratória de dados
- Pré-processamento
- Balanceamento e avaliação de classes
- Padronização dos dados
- Construção de Pipeline
- Treinamento de modelos supervisionados
- Avaliação utilizando métricas de classificação

A implementação demonstra um fluxo completo para problemas de detecção de fraudes, servindo como base para estudos e projetos futuros envolvendo classificação de dados desbalanceados.
