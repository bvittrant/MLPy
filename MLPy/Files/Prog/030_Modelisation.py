###############################################################################

# Modelisation regression

###############################################################################

# Define some path
Datapath = OutputDir+"Results/"+YTarget+"/Data/030_ResTestMetrics_"+YTarget+".tsv"

###############################################################################

# Prepare the model list to iterate depending on the type of problem
if TaskType == "Regression":
    VecModel = [
        ensemble.RandomForestRegressor(n_estimators=500, n_jobs = CPU),
        ensemble.ExtraTreesRegressor(n_estimators=500, n_jobs = CPU),
        ensemble.RandomForestRegressor(n_estimators=1500, n_jobs = CPU),
        ensemble.ExtraTreesRegressor(n_estimators=1500, n_jobs = CPU),
        tree.DecisionTreeRegressor(),
        ensemble.AdaBoostRegressor(),
        neighbors.KNeighborsRegressor(n_jobs = CPU),
        linear_model.LinearRegression(n_jobs = CPU),
        #linear_model.Perceptron(tol=1e-3, random_state=0), ==> problem if target is float
        svm.LinearSVR(tol = 0.01, C = 1),
        svm.LinearSVR(tol = 0.01, C = 0.5),
        #discriminant_analysis.QuadraticDiscriminantAnalysis(reg_param=np.finfo(float).eps), ==> problem if target is float
        #linear_model.SGDRegressor(),
        linear_model.BayesianRidge(),
        #linear_model.LassoLars(),
        #linear_model.ARDRegression(),
        linear_model.PassiveAggressiveRegressor(),
        ]

if TaskType == "Classification":
    VecModel = [
        ensemble.RandomForestClassifier(n_estimators=500, n_jobs = CPU),
        ensemble.ExtraTreesClassifier(n_estimators=500, n_jobs = CPU),
        ensemble.RandomForestClassifier(n_estimators=1500, n_jobs = CPU),
        ensemble.ExtraTreesClassifier(n_estimators=1500, n_jobs = CPU),
        tree.DecisionTreeClassifier(),
        ensemble.AdaBoostClassifier(),
        neighbors.KNeighborsClassifier(n_jobs = CPU),
        linear_model.LogisticRegression(n_jobs = CPU, solver = 'lbfgs'),
        linear_model.Perceptron(tol=1e-3, random_state=0),
        svm.SVC(tol = 0.01, kernel = "rbf", C = 1, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "rbf", C = 0.5, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "poly", C = 1, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "poly", C = 0.5, gamma = "scale"),
        discriminant_analysis.QuadraticDiscriminantAnalysis(reg_param=np.finfo(float).eps)
        ]

if TaskType == "Multiclass-Classification":
    VecModel = [
        ensemble.RandomForestClassifier(n_estimators=500, n_jobs = CPU),
        ensemble.ExtraTreesClassifier(n_estimators=500, n_jobs = CPU),
        ensemble.RandomForestClassifier(n_estimators=1500, n_jobs = CPU),
        ensemble.ExtraTreesClassifier(n_estimators=1500, n_jobs = CPU),
        tree.DecisionTreeClassifier(),
        naive_bayes.BernoulliNB(),
        naive_bayes.GaussianNB(),
        neighbors.KNeighborsClassifier(n_jobs = CPU),
        linear_model.LogisticRegression(multi_class="multinomial", n_jobs=CPU, solver = "lbfgs"),
        linear_model.Perceptron(tol=1e-3, random_state=0),
        svm.SVC(tol = 0.01, kernel = "rbf", C = 1, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "rbf", C = 0.5, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "poly", C = 1, gamma = "scale"),
        svm.SVC(tol = 0.01, kernel = "poly", C = 0.5, gamma = "scale"),
        discriminant_analysis.QuadraticDiscriminantAnalysis(reg_param=np.finfo(float).eps)
        ]

###############################################################################

# Create empty DF to pick up mape score and all the others metrics needed
DfResTest = pd.DataFrame()

###############################################################################

# Run the modelisation depending on the type of problem
if TaskType == "Regression":
    # First loop is to iterate with a specific number of features.
    for j in tqdm(range(Nb_features_intoModelMin, (Nb_features_intoModelMax+1),  Nb_features_step)) :
        # Create sample "iterable" on test set
        iterable = []
        for i in range(1, (Nb_sampling+1)):
            iterable.append([i])
        # Create partial function for var that don't change in pool sampling function
        Partial_sampling = partial(Pool_sampling_reg, SelectedFeatures, Data, YTarget, VecModel, j)
        # Run the pool part with specific number of CPU
        p = Pool(CPU_pool)
        tmp = p.starmap(Partial_sampling, iterable)
        # Unlist item collected by starmap
        tmp = [item for sublist in tmp for item in sublist]
        # Transform the list in dataframe
        tmp = pd.DataFrame(tmp)
        # Concatenate the different items in a dataframe
        DfResTest = DfResTest.append(tmp)
        #print(tmp)
        p.close()

    # Define DF colnames
    DfResTest.columns = ["Model", "NbOfFeatures", "Sampling", 'MAE', 'MedAE',"MSE"] # "RMSE"
    # Merge list and save it in file
    DfResTest.to_csv(path_or_buf = Datapath, header = True, index = False, sep = "\t") # sep = tabulation
       
if TaskType == "Classification":
    # First loop is to iterate with a specific number of features.
    for j in tqdm(range(Nb_features_intoModelMin, (Nb_features_intoModelMax+1),  Nb_features_step)) :
        # Create sample "iterable" on test set
        iterable = []
        for i in range(1, (Nb_sampling+1)):
            iterable.append([i])
        # Create partial function for var that don't change in pool sampling function
        Partial_sampling = partial(Pool_sampling_class, SelectedFeatures, Data, YTarget, VecModel, j)
        # Run the pool part with specific number of CPU
        p = Pool(CPU_pool)
        tmp = p.starmap(Partial_sampling, iterable)
        # Unlist item collected by starmap
        tmp = [item for sublist in tmp for item in sublist]
        # Transform the list in dataframe
        tmp = pd.DataFrame(tmp)
        # Concatenate the different items in a dataframe
        DfResTest = DfResTest.append(tmp)
        #print(tmp)
        p.close()

    # Define DF colnames
    DfResTest.columns = ["Model", "NbOfFeatures", "Sampling", 'ACC', 'AUC',"MatCoef"] 
    # Merge list and save it in file
    DfResTest.to_csv( path_or_buf = Datapath, header = True, index = False, sep = "\t") # sep = tabulation

if TaskType == "Multiclass-Classification":
    # First loop is to iterate with a specific number of features.
    for j in tqdm(range(Nb_features_intoModelMin, (Nb_features_intoModelMax+1),  Nb_features_step)) :
        # Create sample "iterable" on test set
        iterable = []
        for i in range(1, (Nb_sampling+1)):
            iterable.append([i])
        # Create partial function for var that don't change in pool sampling function
        Partial_sampling = partial(Pool_sampling_multiclass, SelectedFeatures, Data, YTarget, VecModel, j)
        # Run the pool part with specific number of CPU
        p = Pool(CPU_pool)
        tmp = p.starmap(Partial_sampling, iterable)
        # Unlist item collected by starmap
        tmp = [item for sublist in tmp for item in sublist]
        # Transform the list in dataframe
        tmp = pd.DataFrame(tmp)
        # Concatenate the different items in a dataframe
        DfResTest = DfResTest.append(tmp)
        #print(tmp)
        p.close()

    # Define DF colnames
    DfResTest.columns = ["Model", "NbOfFeatures", "Sampling", 'ACC', 'Jaccard',"MatCoef"] 
    # Merge list and save it in file
    DfResTest.to_csv( path_or_buf = Datapath, header = True, index = False, sep = "\t") # sep = tabulation

###############################################################################