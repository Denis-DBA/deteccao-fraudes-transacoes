# Importa a biblioteca pandas para carregar e manipular os dados
import pandas as pd

# Importa a função responsável por separar dados de treino e teste
from sklearn.model_selection import train_test_split

# Importa a classe Pipeline para organizar as etapas do modelo
from sklearn.pipeline import Pipeline

# Importa o StandardScaler para padronizar os dados
from sklearn.preprocessing import StandardScaler

# Importa o modelo de Regressão Logística
from sklearn.linear_model import LogisticRegression

# Importa as métricas utilizadas na avaliação
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)


# URL pública do dataset
URL_DATASET = (
    "https://storage.googleapis.com/download.tensorflow.org/"
    "data/creditcard.csv"
)


def carregar_dados():
    """
    Carrega o dataset de transações financeiras.
    """

    print("Carregando o dataset...")

    # Lê o arquivo CSV diretamente da URL
    df = pd.read_csv(URL_DATASET)

    # Exibe o tamanho do dataset
    print(
        f"Dataset carregado com "
        f"{df.shape[0]} linhas e {df.shape[1]} colunas."
    )

    return df


def preparar_dados(df):
    """
    Separa as variáveis independentes, a variável alvo
    e os conjuntos de treino e teste.
    """

    # Remove a coluna Class e armazena as variáveis independentes
    X = df.drop("Class", axis=1)

    # Armazena a variável alvo
    y = df["Class"]

    # Divide os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    return X_train, X_test, y_train, y_test


def criar_pipeline():
    """
    Cria o pipeline de Machine Learning.
    """

    pipeline = Pipeline([
        (
            "scaler",
            StandardScaler()
        ),
        (
            "model",
            LogisticRegression(
                max_iter=1000,
                class_weight="balanced"
            )
        )
    ])

    return pipeline


def avaliar_modelo(modelo, X_test, y_test):
    """
    Realiza previsões e calcula as métricas do modelo.
    """

    # Gera as classes previstas
    y_pred = modelo.predict(X_test)

    # Gera a probabilidade da classe fraude
    y_prob = modelo.predict_proba(X_test)[:, 1]

    # Calcula as métricas
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    # Exibe os resultados
    print("\nResultados do modelo")
    print("-" * 30)
    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-Score : {f1:.4f}")
    print(f"AUC      : {auc:.4f}")


def executar_pipeline():
    """
    Executa todas as etapas do projeto.
    """

    # Carrega os dados
    df = carregar_dados()

    # Prepara os dados
    X_train, X_test, y_train, y_test = preparar_dados(df)

    # Cria o modelo
    modelo = criar_pipeline()

    print("\nTreinando o modelo...")

    # Treina o pipeline
    modelo.fit(X_train, y_train)

    print("Treinamento concluído.")

    # Avalia o modelo
    avaliar_modelo(
        modelo,
        X_test,
        y_test
    )


# Executa o script somente quando o arquivo é chamado diretamente
if __name__ == "__main__":
    executar_pipeline()
