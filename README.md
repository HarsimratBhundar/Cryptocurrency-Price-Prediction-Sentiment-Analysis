# Cryptocurrency-Price-Prediction---Sentiment-Analysis

A sentiment analysis based approach on prediciting cryptocurrency. 
The program uses Natural Language Processing on top articles on the topic (bitcoin) from the past 9 months, and assigns a sentiment score to each date.
Given the small size of the data, the program uses machine learning models where few features are important inorder (such as a Support Vector Machine, Multi-layer Perceptron, Bernoulli Naive Bayes and Deciscion Tree) to avoid overtraining.

The program selects the best model based on prediction performance which is currently the Bernoulli Naive Bayes, with a prediction accuracy of 65% which is impressive keeping in mind that the data set consists of only 275 points.
