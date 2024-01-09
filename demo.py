from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[110, 30], [140, 40], [170, 65], [180, 80], [175, 78], [150, 50], [165, 55]]  # Features ([height, weight])
Y = ['child', 'child', 'teenager', 'adult', 'adult','teenager', 'teenager']  # Labels (age group)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, Y_train)

# test with single prediction
prediction = clf.predict([[155, 56]]) # prediction: teenager
print(prediction)

# test overall accuracy
predictions = clf.predict(X_test)
print(accuracy_score(Y_test, predictions))
