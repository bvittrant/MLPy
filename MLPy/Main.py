###############################################################################
# Main
# Benjamin Vittrant
###############################################################################

# Test of a possible tool to automatize machine learning pipeline

# python main.py -in .\Data\PH123_D3D0_Change_LogRelabun_data_2019-09-05_10-36-27.csv -tar death_j16 -ID ShortName -ou ..\..\misc\  -ma 100 -cpupool 3 -sc Yes -sa 100 -ex 0

###############################################################################
# Import libraries and functions
###############################################################################

exec(open("Files/Prog/000_FromImport.py").read())

# To modify by implementing real import
# (import not working currently don't know why so i use a classic exec open )
exec(open("Files/Prog/001_HomeFunctions.py").read())

###############################################################################

if __name__ == '__main__':

    ###########################################################################
    # Manage user input
    
    exec(open("Files/Prog/003_ManageUserInput.py").read())
    exec(open("tmp.py").read())

    ###########################################################################
    # Define specific parameters for further analysis
    print("\nRead user info and manage directory\n")

    DateTime = datetime.now()

    exec(open("User_info.py").read())

    # Create dir
    exec(open("Files/Prog/002_ManageDirectory.py").read())

    ###########################################################################
    # Task preparation
    ###########################################################################

    print("Task preparation\n")

    exec(open("Files/Prog/010_TaskPreparation.py").read())

    ###########################################################################
    # Features ranking
    ###########################################################################

    print("Features ranking\n")

    exec(open("Files/Prog/020_FeaturesRanking.py").read())

    ###########################################################################
    # Modelisation
    ###########################################################################

    print("Modelisation\n")

    exec(open("Files/Prog/030_Modelisation.py").read())

    ###########################################################################
    # Graphics and summary on benchmark
    ###########################################################################

    print("\nGraphics and summary on benchmark\n")

    exec(open("Files/Prog/040_Graphics.py").read())

    ###########################################################################
    # Test on external set
    ###########################################################################

    print("Test on external set\n")

    exec(open("Files/Prog/050_External.py").read())

    ###########################################################################

    print("Cleaning\n")

    exec(open("Files/Prog/060_Clean.py").read())

    ###########################################################################

    print("Analyse ended\n")