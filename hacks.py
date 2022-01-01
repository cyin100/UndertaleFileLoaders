#todo
#TOPCAKE/REVIVEBRITE
#EVERYBODYWEAPON
#DEALMAKER (ch2) JEVILSTAIL (ch1)

#BUTTERSCOTCH PIE
#REALKNIFE
#THELOCKET

HACK = 'snowgrave'
WRITETO = 'BACKUP\\filech2_0'
copy = 'DELTARUNE\\snowgrave_ending\\filech2_0'

if HACK == 'snowgrave':

    inputFile = open(copy, 'r')
    hacked_data = inputFile.readlines()

    file = open(WRITETO, 'r')
    data = file.readlines()
    file.close()

    file = open(WRITETO, 'w')

    for i in range(264):
        file.write(data[i])
    for i in range(264, 325):
        file.write(hacked_data[i])
        print(hacked_data[i])
    for i in range(325, len(data)):
        file.write(data[i])
    
    file.close()
    inputFile.close()

    