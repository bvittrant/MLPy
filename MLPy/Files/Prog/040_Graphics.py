###############################################################################
# Benjamin Vittrant
# December 2019
###############################################################################

# Graphics and summary on benchmark

###############################################################################

# Prepare the data to be used

# Load the data from previous step
ResTestMetrics = pd.read_csv(OutputDir+"Results/"+YTarget+"/Data/030_ResTestMetrics_"+YTarget+".tsv",
header = 0, sep = '\t')

# create empty column to pick up futur model short name
ResTestMetrics['ModelShort'] = ""
# Create a new vector with full model name and a number
ListModel = ResTestMetrics['Model'].unique()
for i in range(ResTestMetrics.shape[0]):
    # Split the long model name on ( to get only the sort name)
    ResTestMetrics.loc[i,'ModelShort'] = ResTestMetrics.loc[i,'Model'].split("(")[0] + "_" + str(ListModel.tolist().index(ResTestMetrics.loc[i,'Model']))

# Melt the data for more graphic convenient use
ResTestMetricsMelt = pd.melt(ResTestMetrics, id_vars=['Model','NbOfFeatures','Sampling', 'ModelShort'])

# Add mean and median value by Model & NbOffeatures
ResTestMetricsMelt['Mean'] = ResTestMetricsMelt.groupby(['Model','NbOfFeatures','variable',]).value.transform('mean')
ResTestMetricsMelt['Median'] = ResTestMetricsMelt.groupby(['Model','NbOfFeatures','variable',]).value.transform('median')

# Select and save the link between Model and ModelShort
ResTestMetrics.loc[0:len(ListModel),['Model', 'ModelShort']].to_csv( path_or_buf = OutputDir+"Results/"+YTarget+"/Data/040_LinkModelShortName_"+YTarget+".tsv", header = True, index = False, sep = "\t") # sep = tabulation

###############################################################################

# Corrplot

###############################################################################

# Compute correlation matrix for the selected features
corr = Data[SelectedFeatures].corr()

# Seaborn plot
# Set xlabels if not too much
if(len(SelectedFeatures) > 30):
    sns_plot = sns.heatmap(
        corr, 
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True,
        xticklabels=False,
        yticklabels=False
    )
else :
    sns_plot = sns.heatmap(
        corr, 
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
# Save the plot
sns_plot.figure.savefig(OutputDir+"Results/"+YTarget+"/Pictures/Feature_score_correlation_"+YTarget+".pdf", bbox_inches="tight")

###############################################################################

# Graphics: Ranking features

###############################################################################

for n in [ round(NbFeatures/5), round(NbFeatures/2),NbFeatures, round(feature_scores.shape[0]/10),
round(feature_scores.shape[0]/2), feature_scores.shape[0]]:
    # Open graphical pannel
    plt.rcdefaults()
    fig, ax = plt.subplots()
    # Data
    Features = feature_scores.index[:n]
    y_pos = np.arange(n)
    Score = feature_scores.iloc[0:n, 0]
    # Plot 
    ax.barh(y_pos, Score, align='center')
    ax.set_yticks(y_pos)
    if n < 31:
        ax.set_yticklabels(Features)
    if n > 30:
        ax.get_yaxis().set_visible(False)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_title('Mutual information')
    plt.savefig(OutputDir+"Results/"+YTarget+"/Pictures/Feature_score_"+YTarget+"_"+str(n)+".pdf", bbox_inches="tight")
    plt.close()

###############################################################################

# Graphics: subplot by metrics for each model

###############################################################################

for model in ResTestMetricsMelt['Model'].unique():

    # Open graphical pannel
    plt.rcdefaults()
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20,10))
    fig.subplots_adjust(hspace=0.3)

    # add a subplot for each metric
    comp = 1
    for metric in ResTestMetricsMelt['variable'].unique():

        tmp = ResTestMetricsMelt[(ResTestMetricsMelt['Model'] == model) & (ResTestMetricsMelt['variable'] == metric)]

        # Add the value we want f(x,y)
        eval(("ax"+str(comp))).plot(tmp["NbOfFeatures"], tmp["Median"])
        # Add y label
        eval(("ax"+str(comp))).set_ylabel(metric)
        # Add a grid
        eval(("ax"+str(comp))).grid(True)
        # Remove x ticks on first 2 plots
        if ("ax"+str(comp)) == "ax1" or eval(("ax"+str(comp))) == "ax2":
            eval(("ax"+str(comp))).set_xticklabels([])
        comp = comp + 1
    
    ax1.set_title(model)
    ax3.set_xlabel("Nb of features")
    plt.savefig(OutputDir+"Results/"+YTarget+"/Pictures/Model_"+YTarget+"_"+tmp['ModelShort'].unique()[0]+"_"+".pdf", bbox_inches="tight")
    plt.close()

###############################################################################

# Graphics: One plot per metric with all model

###############################################################################

for metric in ResTestMetricsMelt['variable'].unique():

    # Open graphical pannel
    plt.rcdefaults()
    fig, ax = plt.subplots(1, 1, figsize=(20,10))

    # Add all line from the differents models
    for model in ResTestMetricsMelt['Model'].unique():
        tmp = ResTestMetricsMelt[(ResTestMetricsMelt['Model'] == model) & (ResTestMetricsMelt['variable'] == metric)]
        ax.plot(tmp["NbOfFeatures"], tmp["Median"], label = tmp['ModelShort'].unique()[0])
    
    # Add y label
    ax.set_ylabel(metric)
    # Add a grid
    ax.grid(True)
    # Add the legend (come from label option)
    chartBox = ax.get_position()
    ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.6, chartBox.height])
    ax.legend(loc='upper center', bbox_to_anchor=(1.45, 0.8), shadow=True, ncol=1)
    plt.savefig(OutputDir+"Results/"+YTarget+"/Pictures/Model_"+YTarget+"_"+"_Metric_"+metric+".pdf", bbox_inches="tight")
    plt.close()