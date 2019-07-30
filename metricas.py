# -*- coding: utf-8 -*-
import nltk

from difflib import SequenceMatcher
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def exactMatch(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if str1 == str2:
        return 1
    return 0

def longestSubstringNormalized(str1,str2):
    # initialize SequenceMatcher object with
    # input string

    str1 = str1.lower()
    str2 = str2.lower()

    seqMatch = SequenceMatcher(None,str1,str2)
    # find match of longest sub-string
    # output will be like Match(a=0, b=0, size=5)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))
    # print longest substring
    if (match.size!=0):
        #print(match.size)
        #print(len(str1))
        #print(len(str2))
        a = len(str1) + len(str2)
        #print("size of thge two strings - ", a)
        b = a / 2
        #print(b)
        #print("size of thge two strings divided by 2: %f" % b)
        #print(match.size / b)
        return (match.size / b)

    return 0

def lcssNormalized(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    # find the length of the strings
    m = len(str1)
    n = len(str2)

    # declaring the array for storing the dp values
    L = [[None]*(n + 1) for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return (L[m][n] / ((m + n) / 2) )

def edit_distance(str1, str2):
    return nltk.edit_distance(str1.lower(), str2.lower())

def jaccard_distance(str1, str2):
    return nltk.jaccard_distance(set(str1.lower()), set(str2.lower()))

def cosine_similarity_with_tf_idf(tfidf_vectorizer, str1, str2):#[registro['G_aboutme'], registro['T_Description']])
    tfidf_matrix = tfidf_vectorizer.fit_transform([str1.lower(), str2.lower()])
    X = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
    return X[0][1]


def get_metricas_username(str1, str2):
    # 1 é bom, 0 é ruim
    username_em   = exactMatch(str1, str2)

    # quanto maior, melhor (de 0 até 1)
    username_lcs  = longestSubstringNormalized(str1, str2)

    # quanto maior, melhor (de 0 até 1)
    username_lcss = lcssNormalized(str1, str2)

    # quanto menor, melhor (valor absoluto)
    username_ld   = edit_distance(str1, str2)

    # quanto menor, melhor (de 0 até 1)
    username_js   = jaccard_distance(str1, str2)

    return [username_em, username_lcs, username_lcss, username_ld, username_js]


def get_metricas_fullname(str1, str2):
    # 1 é bom, 0 é ruim
    fullname_em   = exactMatch(str1, str2)

    # quanto maior, melhor (de 0 até 1)
    fullname_lcs  = longestSubstringNormalized(str1, str2)

    # quanto maior, melhor (de 0 até 1)
    fullname_lcss = lcssNormalized(str1, str2)

    # quanto menor, melhor (valor absoluto)
    fullname_ld   = edit_distance(str1, str2)

    # quanto menor, melhor (de 0 até 1)
    fullname_js   = jaccard_distance(str1, str2)

    return [fullname_em, fullname_lcs, fullname_lcss, fullname_ld, fullname_js]

def get_metricas_location(str1, str2):
     # 1 é bom, 0 é ruim
    location_em  = exactMatch(str1, str2)

    # quanto maior, melhor (de 0 até 1)
    location_lcs = longestSubstringNormalized(str1, str2)

    # quanto menor, melhor (de 0 até 1)
    location_js  = jaccard_distance(str1, str2)

    return [location_em, location_lcs, location_js]

def get_metricas_description(tfidf_vectorizer, str1, str2):
    # quanto maior, melhor (de 0 até 1)
    description_cs = cosine_similarity_with_tf_idf(tfidf_vectorizer, str1, str2)

    return [description_cs]

def get_dict_metricas(vec_username, vec_fullname, vec_location, vec_description):

    vec_username_features    = get_metricas_username(vec_username[0], vec_username[1])
    vec_fullname_features    = get_metricas_fullname(vec_fullname[0], vec_fullname[1])
    vec_location_features    = get_metricas_location(vec_location[0], vec_location[1])
    vec_description_features = get_metricas_description(vec_description[0], vec_description[1], vec_description[2])

    return [
        vec_username_features[0],
        vec_username_features[1],
        vec_username_features[2],
        vec_username_features[3],
        vec_username_features[4],
        vec_fullname_features[0],
        vec_fullname_features[1],
        vec_fullname_features[2],
        vec_fullname_features[3],
        vec_fullname_features[4],
        vec_location_features[0],
        vec_location_features[1],
        vec_location_features[2],
        vec_description_features[0]
    ]

def extrair_caracteristicas(dataset):
    # =============================================================================
    # O for abaixo gera a lista de dicionarios contendo as caracteristicas
    # de cada registro.
    #
    # no google, username é o G_Displayname;
    # no twitter, username é o T_ScreenName;
    #
    # no google, fullname é o "G_Firstname"+" "+"G_Lastname";
    # no twitter, fullname é o T_Fullname;
    # =============================================================================

    tfidf_vectorizer = TfidfVectorizer()
    caracteristicas  = []

    for registro in dataset:

        g_fullname = registro['g_plus']['G_Firstname'] + " " + registro['g_plus']['G_Lastname']

        vec_username    = [registro['g_plus']['G_Displayname'], registro['twitter']['T_ScreenName']]
        vec_fullname    = [g_fullname, registro['twitter']['T_Fullname']]
        vec_location    = [registro['g_plus']['G_Location'], registro['twitter']['T_Location']]
        vec_description = [tfidf_vectorizer, registro['g_plus']['G_aboutme'], registro['twitter']['T_Description']]

        aux = get_dict_metricas(
            vec_username,
            vec_fullname,
            vec_location,
            vec_description
        )

        caracteristicas.append(aux)

    return caracteristicas