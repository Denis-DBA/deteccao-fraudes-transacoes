# 📄 Relatório do Projeto

# 🚨 Detecção de Fraudes em Transações com Cartão de Crédito

## 📌 Visão Geral

Este projeto tem como objetivo desenvolver e comparar diferentes abordagens de Machine Learning para identificar transações fraudulentas com cartão de crédito.

Durante o desenvolvimento foram realizadas etapas de análise exploratória dos dados, pré-processamento, treinamento de modelos e avaliação de desempenho, buscando identificar a abordagem mais eficiente para um problema de classificação altamente desbalanceado.

---

# 📊 Dataset

O projeto utiliza o conjunto de dados **Credit Card Fraud Detection**, composto por transações reais de cartões de crédito.

Principais características do dataset:

- Variáveis anonimizadas (**V1** até **V28**)
- Variável **Time**
- Variável **Amount**
- Variável alvo **Class**
  - **0:** Transação não fraudulenta
  - **1:** Transação fraudulenta

O conjunto de dados apresenta um forte desbalanceamento entre as classes, característica comum em problemas de detecção de fraudes.

---

# 🧹 Pré-processamento

As principais etapas realizadas foram:

- Carregamento da base de dados
- Verificação de valores ausentes
- Análise da distribuição das classes
- Separação das variáveis independentes e da variável alvo
- Divisão dos dados em conjuntos de treinamento e teste
- Padronização das variáveis utilizando **StandardScaler**

---

# 🤖 Abordagens Avaliadas

Durante o projeto foram implementadas cinco abordagens para comparar diferentes estratégias de classificação:

### 1. Logistic Regression

Utilizada como modelo base para estabelecer um desempenho inicial na classificação das transações.

### 2. Pipeline (StandardScaler + Logistic Regression)

Implementação utilizando o **Pipeline** do Scikit-Learn para automatizar a padronização dos dados e o treinamento do modelo em um único fluxo.

### 3. Ajuste do Threshold (0.3)

Alteração do limiar de decisão do modelo de Regressão Logística com o objetivo de aumentar a capacidade de detectar transações fraudulentas, priorizando o Recall.

### 4. Random Forest

Modelo baseado em conjunto de árvores de decisão, utilizado para melhorar a capacidade de classificação em relação à Regressão Logística.

### 5. XGBoost

Modelo baseado em Gradient Boosting, reconhecido pelo excelente desempenho em problemas de classificação e utilizado como última abordagem do projeto.

---

# 📈 Avaliação dos Modelos

Os modelos foram avaliados utilizando as seguintes métricas:

- **Accuracy:** porcentagem de previsões corretas realizadas pelo modelo em relação ao total de transações analisadas.
- **Precision:** mede a proporção de transações classificadas como fraude que realmente eram fraudulentas, indicando a confiabilidade das previsões positivas.
- **Recall:** mede a capacidade do modelo em identificar corretamente as transações fraudulentas, minimizando a quantidade de fraudes não detectadas.
- **F1-score:** média harmônica entre Precision e Recall, oferecendo um equilíbrio entre essas duas métricas, especialmente importante em conjuntos de dados desbalanceados.
- **Matriz de Confusão:** apresenta a quantidade de verdadeiros positivos, verdadeiros negativos, falsos positivos e falsos negativos, permitindo uma análise detalhada do desempenho do modelo.
- **Curva ROC:** gráfico que relaciona a taxa de verdadeiros positivos com a taxa de falsos positivos em diferentes limiares de decisão, permitindo comparar o desempenho dos modelos.
- **Área sob a Curva (AUC):** representa o desempenho geral da Curva ROC. Quanto mais próximo de 1, melhor a capacidade do modelo em distinguir transações fraudulentas das legítimas.

Essas métricas permitiram comparar objetivamente o desempenho das diferentes abordagens implementadas e identificar o modelo mais eficiente para o problema de detecção de fraudes.

---

# 📊 Resultado Final das Abordagens

Após a avaliação dos modelos, foram obtidos os seguintes resultados:

| Abordagem | Resultado |
|-----------|-----------|
| **Logistic Regression** | Modelo base com bom desempenho inicial (**F1-score = 0.74**). |
| **Pipeline (StandardScaler + Logistic Regression)** | Organizou o fluxo de treinamento e manteve o desempenho da Regressão Logística (**F1-score = 0.74**). |
| **Threshold (0.3)** | Aumentou a capacidade de detectar fraudes (Recall), elevando o **F1-score para 0.75**. |
| **Random Forest** | Melhorou significativamente a detecção de fraudes, alcançando **F1-score = 0.79**. |
| **XGBoost** | Apresentou o melhor desempenho, com **Precision = 0.94**, **Recall = 0.78** e **F1-score = 0.85**, sendo a abordagem mais eficaz para este conjunto de dados. |

---

# 🎯 Conclusão

A comparação entre as cinco abordagens demonstrou que diferentes técnicas podem produzir resultados distintos para um mesmo problema de classificação.

Embora a **Logistic Regression** tenha apresentado um bom desempenho inicial, estratégias como o ajuste do **Threshold**, o uso de **Random Forest** e, principalmente, do **XGBoost**, proporcionaram melhorias na identificação de transações fraudulentas.

Entre todas as abordagens avaliadas, o **XGBoost** apresentou o melhor equilíbrio entre **Precision**, **Recall** e **F1-score**, tornando-se o modelo mais eficiente para este conjunto de dados.

Este projeto permitiu aplicar, na prática, conceitos fundamentais de Ciência de Dados e Machine Learning, incluindo análise exploratória, pré-processamento, construção de pipelines, treinamento de modelos supervisionados e comparação de desempenho utilizando métricas de classificação.
