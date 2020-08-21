###############################################################################
# Authors : Benjamin Vittrant
###############################################################################

# Importing library that are needed within the tool

###############################################################################
# Need to be first
import sys
ModuleList = "sys;"+ "no attribute version" + "\n"
###############################################################################
from functools import partial
ModuleList = ModuleList + "functools;" + "No attribute version" + "\n"
###############################################################################
import os
ModuleList = ModuleList + "os;" + "No attribute version" + "\n"
###############################################################################
import multiprocessing
from multiprocessing import Pool
ModuleList = ModuleList + "multiprocessing;" + "No attribute version" + "\n"
###############################################################################
import shutil
ModuleList = ModuleList + "shutil;" + "No attribute version" + "\n"
###############################################################################
# Manage path and directory creation
from pathlib import Path
ModuleList = ModuleList + "pathlib;" + "No attribute version" + "\n"
###############################################################################
# Recommended command line parsing module
import argparse
ModuleList = ModuleList + "argparse;"+ argparse.__version__ + "\n"
###############################################################################
# pandas: Pandas is data science library that help to handle and manage various
# objects as dataframe. Mostly transform python in R.
import pandas as pd
ModuleList = ModuleList + "pandas;"+ pd.__version__ + "\n"
###############################################################################
# scikit-learn: A huge collection of tools for machine learning process and
# pipelines. We all rely on it to live.
import sklearn as sklearn
ModuleList = ModuleList + "sklearn;"+ sklearn.__version__ + "\n"
# Import the scaling function
from sklearn.preprocessing import StandardScaler
# MODEL IMPORT FROM SKLEARN
from sklearn.model_selection import train_test_split
# Import mutual info (Information gain)
from sklearn.feature_selection import mutual_info_classif
# Import mutual info (Information gain)
from sklearn.feature_selection import mutual_info_regression
# Import metrics
from sklearn import metrics
# Import ensemble model
from sklearn import ensemble
# Import DecisionTree model
from sklearn import tree
# Import Naive Bayes
from sklearn import naive_bayes
# Import KNN
from sklearn import neighbors
# Import linear model
from sklearn import linear_model
# Import SVM
from sklearn import svm
# Import QDA
from sklearn import discriminant_analysis
# Import Bayes
from sklearn import naive_bayes
###############################################################################
# matplotlib: Library for various plot. R is better at this game. Personnal
# opinion
import matplotlib
import matplotlib.pyplot as plt
ModuleList = ModuleList + "matplotlib;"+ matplotlib.__version__ + "\n"
###############################################################################
# Seaborn: Also a graph library
import seaborn as sns
ModuleList = ModuleList + "seaborn;"+ sns.__version__ + "\n"
###############################################################################
# numpy: Library for data and math in python
import numpy as np
ModuleList = ModuleList + "numpy;"+ np.__version__ + "\n"
# math: import the math module  
import math
ModuleList = ModuleList + "math;"+ "no attribute version" + "\n"
# statistics: import the statistics module
import statistics
ModuleList = ModuleList + "statistics;"+ "no attribute version" + "\n"
###############################################################################
# ggplot: Graphic library, from R ggplot
#from ggplot import *
###############################################################################
# For progressbar
#import progressbar
from tqdm import tqdm
ModuleList = ModuleList + "tqdm;"+ "no attribute version" + "\n"
###############################################################################
# For time and date ! :) !
import time
ModuleList = ModuleList + "time;"+ "no attribute version" + "\n"
from datetime import datetime
ModuleList = ModuleList + "datetime;"+ "no attribute version" + "\n"
###############################################################################
# Python info version
ModuleList = ModuleList + "python;"+sys.version+ "\n"
###############################################################################
# Create the file HERE it will be move after directories creation
f = open("Session_info.txt", "w")
f.write(ModuleList)
# Close the file
f.close()
