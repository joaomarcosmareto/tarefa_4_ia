# -*- coding: utf-8 -*-
import numpy
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV

from sklearn.metrics import classification_report, confusion_matrix

def tuna_hiperparametros_rfc(treino_dados, treino_resultados):
    # Testa para descobrir o melhor conjunto de hiper-parâmetros para o classificador
    # número de árvores na floresta aleatória
    n_estimators = [int(x) for x in numpy.linspace(start = 200, stop = 2000, num = 10)]
    # número de características em cada split
    max_features = ['auto', 'sqrt']

    # profundidade máxima
    max_depth = [int(x) for x in numpy.linspace(100, 500, num = 11)]
    max_depth.append(None)
    # create random grid
    random_grid = {
        'n_estimators' : n_estimators,
        'max_features' : max_features,
        'max_depth'    : max_depth
    }
    # Random search of parameters
    modelo = RandomForestClassifier()
    rfc_random = RandomizedSearchCV(estimator = modelo, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
    # Fit the model
    rfc_random.fit(treino_dados, treino_resultados)
    return rfc_random

def get_predicao_decision_tree(treino_dados, treino_resultados, teste_dados):
    modelo = DecisionTreeClassifier()

    # Preenche o modelo com dados e labels de treino
    modelo.fit(treino_dados, treino_resultados)

    # Usa o conjunto de dados de teste para tentar prever os resultados
    pred = modelo.predict(teste_dados)

    return pred

def get_predicao_random_forest(rfc_testar_hiperparametros, treino_dados, treino_resultados, teste_dados):
    if rfc_testar_hiperparametros:
    # BEGIN - TRECHO TESTADO EM UM COMPUTADOR COM 16 CORES, E 8 GIGAS DE RAM
    # Testa para descobrir o melhor conjunto de hiper-parâmetros para o classificador
        hiper_params = tuna_hiperparametros_rfc(treino_dados, treino_resultados)
        modelo = RandomForestClassifier(
                n_estimators = hiper_params.best_params_['n_estimators'],
                max_depth    = hiper_params.best_params_['max_depth'],
                max_features = hiper_params.best_params_['max_features'],
        )
    # END - TRECHO TESTADO EM UM COMPUTADOR COM 16 CORES, E 8 GIGAS DE RAM
    else:
        modelo = RandomForestClassifier()

    # Preenche o modelo com dados e labels de treino
    modelo.fit(treino_dados, treino_resultados)

    # Usa o conjunto de dados de teste para tentar prever os resultados
    pred = modelo.predict(teste_dados)

    return pred

def report(teste_resultados, pred):
    #Thus in binary classification, the count of true negatives is 0,0; false negatives is 1,0; true positives is 1,1 and false positives is 0,1.

    a = confusion_matrix(teste_resultados, pred)

    conf_matrix = {}

    conf_matrix["vn"] = a[0][0]
    conf_matrix["vp"] = a[1][1]
    conf_matrix["fn"] = a[1][0]
    conf_matrix["fp"] = a[0][1]

    metricas      = {}
    metricas['0'] = {}
    metricas['1'] = {}

    precisao      = conf_matrix["vp"] / (conf_matrix["vp"] + conf_matrix["fp"])
    sensibilidade = conf_matrix["vp"] / (conf_matrix["vp"] + conf_matrix["fn"])
    f1_score      = 2 * ((precisao * sensibilidade) / (precisao + sensibilidade))
    acuracia      = (conf_matrix["vp"] + conf_matrix["vn"]) / (conf_matrix["vp"] + conf_matrix["fp"] + conf_matrix["fn"] + conf_matrix["vn"])

    metricas['1']['precisao'] = precisao
    metricas['1']['sensibilidade'] = sensibilidade
    metricas['1']['f1_score'] = f1_score
    metricas['1']['acuracia'] = acuracia