###############################################################################
# Benjamin Vittrant
# November 2019
###############################################################################

# Pool sampling function

# Multiprocessing function for sampling step
# In each sampling there is the same actions and computational time
# Except some algo specificity (But it should not be that different in time)
        
###############################################################################
# Multiclass
def Pool_sampling_multiclass(SelectedFeatures, Data, YTarget, VecModel, j, i):
    # Select the features you want to iterate on in the data
    X_train, X_test, y_train, y_test = train_test_split(Data[SelectedFeatures[0:j+1]], Data[YTarget],
    test_size=0.33, stratify=Data[YTarget])
    DfResTestList = []

    # Third loop is to iterate on all model we are testing
    for model in VecModel:
        model.fit(X_train, y_train)
        y_pred_model = model.predict(X_test)
        DfResTestList.append( [model, j, i,
            metrics.accuracy_score(y_test, y_pred_model),
            metrics.jaccard_score(y_test, y_pred_model, average = 'weighted'),
            metrics.matthews_corrcoef(y_test, y_pred_model)] )
        

    return DfResTestList
###############################################################################
# Classification
def Pool_sampling_class(SelectedFeatures, Data, YTarget, VecModel, j, i):
    # Select the features you want to iterate on in the data
    X_train, X_test, y_train, y_test = train_test_split(Data[SelectedFeatures[0:j+1]], Data[YTarget],
    test_size=0.33, stratify=Data[YTarget])
    DfResTestList = []
    # This loop is to iterate on all model we are testing
    for model in VecModel:
                model.fit(X_train, y_train)
                y_pred_model = model.predict(X_test)
                DfResTestList.append( [model, j, i,
                metrics.accuracy_score(y_test, y_pred_model),
                metrics.roc_auc_score(y_test, y_pred_model),
                metrics.matthews_corrcoef(y_test, y_pred_model)
                ] )
        

    return DfResTestList
###############################################################################
# Regression
def Pool_sampling_reg(SelectedFeatures, Data, YTarget, VecModel, j, i):
    # Select the features you want to iterate on in the data
    X_train, X_test, y_train, y_test = train_test_split(Data[SelectedFeatures[0:j+1]], Data[YTarget],
    test_size=0.33) # Regression then not sure it's a good idea to use stratify=Data[YTarget]
    DfResTestList = []
    # This loop is to iterate on all model we are testing
    for model in VecModel:
        model.fit(X_train, y_train)
        y_pred_model = model.predict(X_test)
        DfResTestList.append( [model, j, i,
        metrics.mean_absolute_error(y_test, y_pred_model),
        metrics.median_absolute_error(y_test, y_pred_model),
        metrics.mean_squared_error(y_test, y_pred_model)
        ] )

    # Add specific elasticnet procedure
    elasticnet = linear_model.ElasticNetCV(l1_ratio = [.1, .5, .7, .9, .95, .99, 1] , cv=3,
    random_state=0, n_jobs = 1)
    elasticnet.fit(X_train, y_train)
    y_pred_model = elasticnet.predict(X_test)
    DfResTestList.append( [elasticnet, j, i,
    metrics.mean_absolute_error(y_test, y_pred_model),
    metrics.median_absolute_error(y_test, y_pred_model),
    metrics.mean_squared_error(y_test, y_pred_model)
    ] )

    return DfResTestList
###############################################################################
