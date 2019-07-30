# -*- coding: utf-8 -*-
import metricas
import organiza_datasets
import core

from sklearn.model_selection import train_test_split

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import classification_report, confusion_matrix

input_file = 'teste.json'
input_encoding = 'utf8'

dataset         = []
labels          = []
caracteristicas = []

rfc_testar_hiperparametros = False

# cria o dataset, lendo o json (input_file), removendo os registros com dados nulos ou string vazia;
# cria instancias negativas e concatena num dataset único;
# cria o array de rótulos na mesma ordem que as instancias pareadas e negativas.
dataset, labels = organiza_datasets.build_dificuldade_1(input_file, input_encoding)

# extrai o conjunto de características a partir do dataset
# as características são:
#   Exact Match;
#   Longest Commom Substring;
#   Longest Commom Subsequence;
#   Levenshtein Distance;
#   Jaccard Similarity e;
#   Cosine Similarity with TF-IDF Weights.
caracteristicas = metricas.extrair_caracteristicas(dataset)

# separa o conjunto de características em 70% para treino e 30% para teste
#X_train,     X_test,      y_train,           y_test =           train_test_split(X,               y,)
treino_dados, teste_dados, treino_resultados, teste_resultados = train_test_split(caracteristicas, labels, test_size=0.30)

# obtém a predição a partir da árvore de decisão
pred_decision_tree = core.get_predicao_decision_tree(treino_dados, treino_resultados, teste_dados)

#obtém a predição a partir da random forest
pred_random_forest = core.get_predicao_random_forest(rfc_testar_hiperparametros, treino_dados, treino_resultados, teste_dados)

#faz o relatório contendo matriz de confusao e métricas precisao, sensibilidade (recall), f1-score e acurácia
#a = core.report(teste_resultados, pred_decision_tree)

# Resultado de Cross Validation
#cv_score = cross_val_score(modelo, caracteristicas, labels, cv=10, scoring='roc_auc')

print("=== Confusion Matrix ===")
print(confusion_matrix(teste_resultados, pred_decision_tree))
print('\n')
print("=== Classification Report ===")
print(classification_report(teste_resultados, pred_decision_tree))
print('\n')
#print("=== All AUC Scores ===")
#print(cv_score)
print('\n')
#print("=== Mean AUC Score ===")
#print("Mean AUC Score - Random Forest: ", cv_score.mean())

print("=== Confusion Matrix ===")
print(confusion_matrix(teste_resultados, pred_random_forest))
print('\n')
print("=== Classification Report ===")
print(classification_report(teste_resultados, pred_random_forest))
print('\n')
print("=== All AUC Scores ===")
#print(cv_score)
print('\n')
#print("=== Mean AUC Score ===")
#print("Mean AUC Score - Random Forest: ", cv_score.mean())