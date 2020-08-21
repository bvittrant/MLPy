###############################################################################
# Authors : Benjamin Vittrant
###############################################################################

# Managing directory

###############################################################################

# Create Results arborescense
Path(OutputDir+"Results/"+YTarget+"/Pictures/").mkdir(parents=True, exist_ok=True)
Path(OutputDir+"Results/"+YTarget+"/Summary/").mkdir(parents=True, exist_ok=True)
Path(OutputDir+"Results/"+YTarget+"/Data/").mkdir(parents=True, exist_ok=True)

###############################################################################

# Move session info file after directories creation

shutil.move("Session_info.txt", OutputDir+"Results/"+YTarget+"/Session_info.txt")