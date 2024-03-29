# !pip install scikit-learn xgboost
from sklearn import datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

bst = XGBClassifier(verbosity=3)
bst.fit(X_train, y_train)
preds = bst.predict(X_test)
print(f'preds: {preds}')