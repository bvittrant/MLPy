###############################################################################
# Benjamin Vittrant
# November 2019
###############################################################################

# User info file
# In this file the user define the parameters that will be use in the rest of
# the analysis. If not touched default parameters will be used.

###############################################################################

# Here are the most inmportant info

###############################################################################
# Where is your file ?

# Import your main data file. For now it need to be cleaned and ready to use.
#DataRaw = pd.read_table("Data/Valbiotis.csv", sep = ";", header = 0)
# "Data/Data_multiclass.csv"
DataRaw = pd.read_table(args.Input_file, sep = ";", header = 0)

OutputDir = args.OutputDir

# What is your feature response ?
# death_j16 = Regression / Run # multi-class / Time = binary class 
# Collect argument from user
YTarget = args.Target
# What the name of your column with sample names ?
SampleName = args.SampleID

# How many features do you want to keep in features ranking step ?
NbFeatures = args.Nb_max

###############################################################################

# Info here can stay at defaut

# Maximum number of features to test in the model from the ranking.
# If Nb_features_intoModelMin = 0 & Nb_features_intoModelMax = NbFeatures
# you'll try a model with the first best feature from the ranking then a model
# with 2 ... to a model with Nb_features_intoModelMax. Nb_features_intoModelMax
# should not be superior to NbFeatures.
Nb_features_intoModelMax = NbFeatures
Nb_features_intoModelMin = args.Nb_min # index start at the 0 for a loop
Nb_features_step = args.Nb_step # Step for the iterating loop

# What percentage of your total sample your want to keep for real model
# testing ? It can range from 0 to 1. NOT FINISHED HERE JUST PUT IT TO 0.
PercentageExt = args.Percentage_external

# Number of cpu to use in pool multiprocessing function
CPU_pool = args.CPU_pool

# Number of CPU available to be used in some specific steps
# if set to -1 then all availbale CPU will use
CPU = 1

# Do you want to scale your data ?
# Standardize features by removing the mean and scaling to unit variance
# The standard score of a sample x is calculated as:
# z = (x - u) / s
Scale = args.scale

# Number of resampling per model
Nb_sampling = args.Nb_sampling