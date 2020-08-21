###############################################################################
# Main
# Benjamin Vittrant
# November 2019
###############################################################################

# Modulo commodity function

# Check if a value in List is Modulo R and return a new list with the values
# that match the Modulo R condition.
def Modulo(List, Modulo, R = 0):
        tmp = []
        for i in List:
            if i % Modulo == R:
                tmp.append(i)
        return tmp
        
###############################################################################
