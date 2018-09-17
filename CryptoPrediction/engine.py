import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import BernoulliNB

def getBestModel(models, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.05, random_state = 0)
    
    scaler = StandardScaler()
    X_train_norm = scaler.fit_transform(X_train)
    X_test_norm = scaler.transform(X_test)

    trained_models = list(map(lambda model: model.fit(X_train_norm, y_train), models))
    accuracy_results = list(map(lambda model: accuracy_score(model.predict(X_test_norm), y_test), trained_models))
    
    best_result_index = 0
    for model_index in range(1, len(accuracy_results)):
    	if (accuracy_results[model_index] > accuracy_results[best_result_index]):
    		best_result_index = model_index

    return [trained_models[best_result_index], accuracy_results[best_result_index]]

price_data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/price.csv"))
sentiment_data = pd.read_csv(os.path.join(os.path.dirname(__file__), "data/sent.csv"))

X = sentiment_data.loc[:, ['polarity', 'subjectivity']]
y = []

for i in range(1, len(price_data['price'])):
    if price_data['price'][i] > price_data['price'][i - 1]:
        y.append(1)
    else:
        y.append(0)

models = [SVC(), MLPClassifier(), BernoulliNB(), tree.DecisionTreeClassifier()]

best_model = getBestModel(models, X, y)

print("The best model was: " + str(best_model[0]))
print("The model's accuracy_score was: " + str(best_model[1]))