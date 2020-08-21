###############################################################################

# Preparing data for the rest of the analysis

###############################################################################
# Define some path
DatapathTaskPrep = OutputDir+"Results/"+YTarget+"/Summary/010_TaskPreparation_"+YTarget+".txt"

# Create a file to write the comment about the data
f = open(DatapathTaskPrep, "w+")
f.write("Analyse datetime: {}\n".format(DateTime))
f.write("This files contain informations about your data\n\n")

# Some info about data imported
f.write("You provided me a file with {} column(s) and {} row(s).\n"
    .format(len(DataRaw.columns), len(DataRaw.index) ))
f.write("You choose \"{}\" as your target feature and its type is {}:\n".format(YTarget, DataRaw[YTarget].dtype))

if (DataRaw[YTarget].dtype == 'float64' or DataRaw[YTarget].dtype == 'int64'):
    TaskType = "Regression"
    f.write("==> then your question is a {} problem.\n\n".format(TaskType))

if(DataRaw[YTarget].dtype == 'O' or DataRaw[YTarget].dtype == 'str' ):
    # Force categorical type for string feature
    DataRaw[YTarget] = DataRaw[YTarget].astype('category')
    # Check the feature response and its categories
    tmp = np.unique(DataRaw[YTarget], return_counts=True)
    if tmp[0].shape[0] == 2:
        TaskType = "Classification"
        f.write("   'O' or 'str' then i converted it to a categorical feature and encoded it.\n")
        f.write("==> then your question is a {} problem.\n".format(TaskType))
        f.write("Your response is distributed as:\n")
        f.write("{}\n\n".format(tmp))
        le = sklearn.preprocessing.LabelEncoder()
        le.fit(DataRaw[YTarget])
        # list(le.classes_)
        DataRaw[YTarget] = le.transform(DataRaw[YTarget])
        #DataRaw[YTarget] = list(le.inverse_transform(DataRaw[YTarget]))
    if tmp[0].shape[0] > 2:
        TaskType = "Multiclass-Classification"
        f.write("   'O' or 'str' then i converted it to a categorical feature and encoded it.\n")
        f.write("==> then your question is a {} problem.\n".format(TaskType))
        f.write("Your response is distributed as:\n")
        f.write("{}\n\n".format(tmp))
        le = sklearn.preprocessing.LabelEncoder()
        le.fit(DataRaw[YTarget])
        # list(le.classes_)
        DataRaw[YTarget] = le.transform(DataRaw[YTarget])
        #DataRaw[YTarget] = list(le.inverse_transform(DataRaw[YTarget]))

f.write("You choose to keep {}% of your data set as external validation set.\n\n".format(PercentageExt*100))

###############################################################################

# Drop column with only NA
f.write("Before removing columns with only NA you have {} samples\n".format(len(DataRaw.columns)))
DataRaw = DataRaw.dropna(axis=1, how ='all')
f.write("After removing columns with only NA you have {} samples\n\n".format(len(DataRaw.columns)))

# DROP ROWS WITH NAN
f.write("Before removing rows with at least 1 NA you have {} samples\n".format(len(DataRaw.index)))
DataRaw = DataRaw.dropna()
f.write("After removing rows with at least 1 NA you have {} samples\n\n".format(len(DataRaw.index)))

# Set the index corresponding to selected colname
DataRaw = DataRaw.set_index(SampleName)

# FILTER 0
# Remove rows with ony 0 value
f.write("Before removing column with only 0 value you have {} columns\n".format(len(DataRaw.columns)))
DataRaw = DataRaw.loc[:, (DataRaw != 0).any(axis=0)]
f.write("After removing column with only 0 value you have {} columns\n\n".format(len(DataRaw.columns)))

###############################################################################

# CHECK THIS PART IS IT A GOOD IDEA

# Save and remoive the target from the raw data to avoid to scale it 
SaveTarget = DataRaw.loc[:, DataRaw.columns == YTarget]
DataRaw = DataRaw.loc[:, DataRaw.columns != YTarget]
f.write("Your target will not be scale or dummysied\n\n")

###############################################################################

# SCALING TO STANDARDIZE
NameColRaw = list(DataRaw.columns)
NameRowRaw = list(DataRaw.index)

if(Scale == "Yes"):
    sc = StandardScaler()
    # Select numeric column
    num_cols = DataRaw.columns[DataRaw.dtypes.apply(lambda c: np.issubdtype(c, np.number))]
    # Scale the dataframe
    DataRaw[num_cols] = sc.fit_transform(DataRaw[num_cols])
    # Reconvert the np.array to a dataframe
    DataRaw = pd.DataFrame(DataRaw)

# DUMMIES TRANSFORMATION
# Creating dummies features from character, text features
f.write("Before dummies transformation you have {} features\n".format(len(DataRaw.columns)))
# Transform all non numeric data with dummy transfo except target feature
DataRaw = pd.get_dummies(DataRaw)
f.write("After dummies transformation you have {} features\n\n".format(len(DataRaw.columns)))

###############################################################################

# At the end of dummy step and scaling remerge with the target column
DataRaw.index.names = [SampleName]
DataRaw = pd.merge(DataRaw, SaveTarget, on = SampleName)
del SaveTarget

###############################################################################

# DATA SET CREATION
# PREPARE TRAIN, TEST AND EXTERNAL SET
# Order the data by clearance
DataRaw = DataRaw.sort_values(by=[YTarget])
# Selecte a balanced subset for futur prediction test
# We'll keep PercentageExt of the data
ToKeep = round(PercentageExt*len(DataRaw.index))
if ToKeep == 0:
    ToKeep = 1
# Create a vector of length = nrow with range
# range stop at final value minor 1 , care that.
SEQ = range(0,len(DataRaw.index))
SEQModulo = Modulo(SEQ, round(len(DataRaw.index)/ToKeep))

# Modulo operation to keep balanced sample for futur test
DataValidation = DataRaw.iloc[SEQModulo]
Data = DataRaw.iloc[list(set(SEQ) - set(SEQModulo))]

# Clean object with no further use
del SEQ, SEQModulo, ToKeep

# Close the file
f.close()