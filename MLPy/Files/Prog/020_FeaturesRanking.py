###############################################################################

# Features ranking

###############################################################################

# Define some path

DatapathRanking = OutputDir+"Results/"+YTarget+"/Data/020_FeaturesRanking_"+YTarget+".tsv"
DatapathSelected = OutputDir+"Results/"+YTarget+"/Summary/020_SelectedFeatures_"+YTarget+".txt"

# ADD Feature ranking if task == Regression
if(TaskType == "Regression"):
    
    # MUTUAL INFORMATION RANKING
    # Ranking the features
    feature_scores = mutual_info_regression(Data, Data[YTarget])
    # transforming array in dataframe
    feature_scores = pd.DataFrame(feature_scores)
    # Adding the associated rownames linked to our features ...
    feature_scores.index=Data.columns
    # Order the features to select the best
    feature_scores.sort_values(by = [0], ascending=False, inplace=True)
    # Saving the results to plot
    feature_scores.to_csv(DatapathRanking, header = False, sep = "\t")
    # Removing the target ...
    feature_scores = feature_scores.drop(YTarget)
    # Select feature according to user choice (NbFeatures)
    SelectedFeatures = list(feature_scores.index[:NbFeatures])

# ADD Feature ranking if task == Classification
if(TaskType == "Classification" or TaskType == "Multiclass-Classification"):
    # sklearn.feature_selection.mutual_info_classif(X, y,
    # discrete_features='auto', n_neighbors=3, copy=True, random_state=None)
    # from sklearn.feature_selection import SelectKBest

    # MUTUAL INFORMATION RANKING
    # Ranking the features
    feature_scores = mutual_info_classif(Data, Data[YTarget])
    # transforming array in dataframe
    feature_scores = pd.DataFrame(feature_scores)
    # Adding the associated rownames linked to our features ...
    feature_scores.index=Data.columns
    # Order the features to select the best
    feature_scores.sort_values(by = [0], ascending=False, inplace=True)
    # Saving the results to plot
    feature_scores.to_csv(DatapathRanking, header = False, sep = "\t")
    # Removing the target ...
    feature_scores = feature_scores.drop(YTarget)
    # Select feature according to user choice (NbFeatures)
    SelectedFeatures = list(feature_scores.index[:NbFeatures])

# Export the selected features in file
f = open(DatapathSelected, "w+")
for element in SelectedFeatures:
    f.write(element)
    f.write("\n")
# Close the file
f.close()