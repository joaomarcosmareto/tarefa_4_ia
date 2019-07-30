# tarefa_4_ia
Este é o projeto 4 da disciplina de IA do mestrado em computação aplicada do Ifes campus Serra, turma de 2019-1.
### TAREFA 4 DA DISCIPLINA DE IA

Este é o projeto 4 da disciplina de IA do mestrado em computação aplicada do Ifes campus Serra, turma de 2019-1.

### IDENTIFICAÇÃO DO PROJETO
**Autor:** João Marcos Mareto Calado
<br />
**Linguagem:** Python 3 em sua última versão
<br />
**Ambiente:** Foi utilizado o ambiente anaconda para Windows 10 de 64 bits, com todas as bibliotecas atualizadas
<br />
**Link do artigo no overleaf:** https://www.overleaf.com/read/dsmbqkcwzjyf
<br />
**Template Latex utilizado:** Foi utilizado o template de conferências da SBC

### DESCRIÇÃO DO PROJETO

**Meta:**
<br />
A meta deste projeto é buscar uma forma de resolver os problemas da identificaçã e associação de perfis de usuários em diferentes redes sociais usando os algoritmos de classificação árvore de decisão e floresta aleatória como forma de predizer esta associação de perfis. Este é um problema definido como Cross-system Personalisation" [Carmagnola and Cena 2009].

De acordo com Esfandyari et al. (2018), este é um problema difícil de ser resolvido dada a não estruturação das informações além da falta de garantia na veracidade das informações preenchidas. Corroborando com Esfandyari e colegas, Shu et al. (2017) complementa as dificuldades e desafios da tarefa de identificar os perfis em diferentes redes sociais. São elencados dois motivos pelos quais existe essa dificuldade. O primeiro é que embora usuários tenham contas em diferentes redes, a informação de uma mesma pessoa no mundo real pode ser diversa entre as redes, e o segundo motivo é que as informações da identidade dos usuários é ruidosa, incompleta e altamente não estruturada.

**Materiais e Métodos:**
<br />
Para os experimentos preliminares, será utilizada uma base de dados pública, disponível no portal do Laboratório de Protocolo de Redes e Tecnologias (NPTLab) da Universidade de Milão. A base escolhida será a que contém registros do Google+ e Twitter e foi criada por Esfandyari et al em 2018.

A abordagem seguida é realizar a leitura de dados da base e após isto, sanear a base, removendo-se os registros cujos atributos possuem valor null ou string vazia.

Após esta etapa de saneamento, é gerado um conjunto de instâncias negativas, isto é, registros cujos perfis não são pertencentes à mesma pessoa real. Esta etapa é necessária para que seja possível a implementação de um classificador com dados balanceados.

Em seguida, as seguintes métricas são aplicadas no conjunto de dados:

- 1. Exact Match (EM): Verifica se duas strings são iguais. Retorna 0 ou 1;
- 2. Longest Common Substring (LCS): Medida que verifica o quanto duas strings são iguais. Esta medida é normalizada dividindo o tamanho da maior substring pela média do comprimento das duas strings originais, de modo que o valor desta medida varie entre 0 e 1. Retorna um valor entre 0 e 1;
- 3. Longest Common Sub-Sequence (LCSS): Medida parecida com a LCS, porém de forma que a sequência não precise ser contígua. Novamente o valor de retorno é normalizado pela média do tamanho das duas strings orignais, de modo que o valor desta medida varie entre 0 e 1. Retorna um valor entre 0 e 1;
- 4. Levenshtein Distance (LD): Também conhecido como Edit-Distance, esta medida calcula o menor número de alterações para que uma string fique igual à outra. Retorna um valor inteiro;
- 5. Jaccard Similarity (JS): Medida utilizada para computar sobreposições, definida como o tamanho da interseção divida pelo tamanho da união das amostras;
- 6. Cosine Similarity with TF-IDF Weights: A similaridade de coseno com pesos tf-idf mede a similaridade de textos em termos de ângulo entre as representações desses textos no Modelo de Espaço Vetorial.

As medidas EM, LCS, LCSS, LD e JS são empregadas para comparar os campos baseados em nome (Full Name e Screen Name), e as medidas EM, LCS, e JS são utilizadas para computar a similaridade do campo localização. Para o campo descrição, é utilizada a medida de Cosine Similarity with TF-IDF Weights.

Os campos baseados em nome são Fullname e Username.
- 1. Fullname existe no dataset original como campo pertencente ao twitter, no entanto, para este trabalho, foi necessário criar o campo Fullname nos campos do Google+ concatenando o campo firstname com o campo lastname.
- 2. Username existe no dataset original como Displayname no Google+ e Screenname no Twitter

O campo localização existe no dataset com o mesmo nome tanto no twitter como no Google+ e o campo descrição existe no dataset como aboutme no Google+ e description no Twitter.

Após esta etapa, a lista de dados contendo as características são separados em dois conjuntos, sendo um para treino e outro para testes. O conjunto de treino é utilizado para treinar dois classificadores, sendo um do tipo Árvore de Decisão e outro do tipo Floresta Aleatória. Os modelos serão utilizados para predizer os dados contidos no conjunto de testes.

Os resultados são apresentados sob a forma de matriz de confusão e relatório de classificação.

A matriz de confusão C é uma matriz onde C<sub>i,j</sub> é igual ao número de observações conhecidas por pertencerem ao grupo <em>i</em>, mas predizidas como pertencerem no grupo <em>j</em>.

Portanto, em classificação binária, a contagem de verdadeiros negativos são C<sub>0,0</sub>, falsos negativos são C<sub>1,0</sub>, verdadeiros positivos são C<sub>1,1</sub> e falsos positivos são C<sub>0,1</sub>.

Já o relatório de classificação retorna um dicionário contendo os valores para as medidas <em>precision, recall, f1-score e support</em>, contendo ainda a informação de acurácia.

O resultado esperado é que o classificador floresta aleatória se saia melhor, pois ele utiliza diversas árvores de decisão para fazer a classificação.

### Bibliografia Relevante
BREIMAN, Leo. Random forests.Machine learning, Springer, v. 45, n. 1, p. 5–32, 2001.
<br /><br />
CARMAGNOLA, Francesca; CENA, Federica. User identification for cross-systempersonalisation.Information Sciences, v. 179, n. 1, p. 16–32, 2009. ISSN 0020-0255.Disponível em: <http://www.sciencedirect.com/science/article/pii/S0020025508003551>.
<br /><br />
ESFANDYARI, Azadeh et al. User identification across online social networks in practice:Pitfalls and solutions.Journal of Information Science, SAGE Publications Sage UK:London, England, v. 44, n. 3, p. 377–391, 2018.
<br /><br />
OSHIRO, Thais Mayumi.Uma abordagem para a construção de uma única árvore apartir de uma Random Forest para classificação de bases de expressão gênica. 2013. 101 f.Dissertação (Mestrado em Bioinformática) — Universidade de São Paulo, São Paulo, 2013.
<br /><br />
PERITO, Daniele et al. How unique and traceable are usernames? In: SPRINGER.International Symposium on Privacy Enhancing Technologies Symposium. [S.l.], 2011. p.1–17.
<br /><br />
POWERS, David Martin. Evaluation: from precision, recall and f-measure to roc,informedness, markedness and correlation. Bioinfo Publications, 2011.SHU, Kai et al. User identity linkage across online social networks: A review.Acm SigkddExplorations Newsletter, ACM, v. 18, n. 2, p. 5–17, 2017.
<br /><br />
STEHMAN, Stephen V. Selecting and interpreting measures of thematic classificationaccuracy.Remote sensing of Environment, Elsevier, v. 62, n. 1, p. 77–89, 1997.
<br /><br />
VOSECKY, Jan; HONG, Dan; SHEN, Vincent Y. User identification across multiplesocial networks. In: IEEE.2009 first international conference on networked digitaltechnologies. [S.l.], 2009. p. 360–365.
<br /><br />
WASSERMAN, Stanley; GALASKIEWICZ, Joseph.Advances in social network analysis:Research in the social and behavioral sciences. Sage publications. Califórnia, CA: Sage,1994.
<br /><br />
WITTEN, Ian H.; FRANK, Eibe.Data Mining: Practical machine learning tools andtechniques. Elsevier. San Francisco, CA: Morgan Kaufmann, 2005.
<br /><br />
ZAFARANI, Reza; LIU, Huan. Connecting corresponding identities across communities.In:Third International AAAI Conference on Weblogs and Social Media. [S.l.: s.n.], 2009.
<br /><br />
ZAFARANI, Reza; LIU, Huan. Connecting users across social media sites: abehavioral-modeling approach. In: ACM.Proceedings of the 19th ACM SIGKDDinternational conference on Knowledge discovery and data mining. [S.l.], 2013. p. 41–49.
<br /><br />

### PROGRAMA DESENVOLVIDO
**O programa desenvolvido é:**
* teste.py

**Dependências:**
* sklearn, nltk, numpy  difflib

**Forma de Build:**
* Não é necessário que se faça build do projeto, mas é necessário que as dependências estejam devidamente instaladas.

- 1. Executar o arquivo teste.py
    ``python teste.py``
