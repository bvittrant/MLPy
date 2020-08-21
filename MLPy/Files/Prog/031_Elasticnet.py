###############################################################################
# Benjamin Vittrant
# February 2020
###############################################################################

# Elasticnet approach

###############################################################################

X_train, X_test, y_train, y_test = train_test_split(Data[SelectedFeatures[0:j+1]], Data[YTarget],
    test_size=0.33, stratify=Data[YTarget])

from sklearn.datasets import make_regression
X, y = make_regression(n_features=2, random_state=0)
regr = linear_model.ElasticNetCV(l1_ratio = [.1, .5, .7, .9, .95, .99, 1] , cv=10,
random_state=0, n_jobs = 1)
regr.fit(X, y)
print(regr.alpha_)
print(regr.intercept_)
print(regr.predict([[0, 0]]))