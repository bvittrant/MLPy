###############################################################################
# Benjamin Vittrant
# February 2020
###############################################################################

# Parser file

###############################################################################
# Create parser to pick up user input 
parser = argparse.ArgumentParser()
###############################################################################
# Parser for YTarget response from user 
parser.add_argument("-tar","--Target", help = "Name of your response feature",
type = str)
###############################################################################
# Parser for sample ID (kind of rownames) from user 
parser.add_argument("-ID", "--SampleID", help = "Name of your column containing the sample ID",
type = str)
###############################################################################
# Parser for the number of features to check
parser.add_argument("-ma", "--Nb_max",
help="Maximal number of features you want in the benchmark. Must be > Nb_min.",
type = int, default = 10, required = False)
parser.add_argument("-mi", "--Nb_min",
help="Minimal number of features you want in the benchmark. Must be < Nb_max. Cannot be 0 ...",
type = int, default = 1, required = False)
###############################################################################
# Parser for the iteration on specific number of features
parser.add_argument("-st", "--Nb_step", help="Step on iterating features.", type=int,
default = 1, required = False)
###############################################################################
# Percentage of features to keep as external test set
parser.add_argument("-ex", "--Percentage_external",
help="Percentage of features to consider as external text set from the raw data.",
type=int, default = 0.2, required = False)
###############################################################################
# Number of cpu to use in the pool python multiprocessing part
parser.add_argument("-cpupool", "--CPU_pool",
help="Number of cpu to use in the pool python multiprocessing part.",
type=int, default = 1, required = False)
###############################################################################
# Parser to scale the numeric data
parser.add_argument("-sc", "--scale",
help="Do you want to scale your numerical data.",
type=str, default = "yes", required = False)
###############################################################################
# Parser to set up number of sampling
parser.add_argument("-sa", "--Nb_sampling",
help="How many subsampling do you want ? I recommand to stuck this number to CPU_pool.",
type=int, default = 100, required = False)
###############################################################################
# Parser to pick up working file
parser.add_argument("-in", "--Input_file",
help="Path the file with your data",
type=str, required = True)
###############################################################################
# Parser to set up output result directory
parser.add_argument("-out", "--OutputDir",
help="Set up output directory",
type=str, required = True)
###############################################################################
# Save all arg in a specific object
args = parser.parse_args()
###############################################################################