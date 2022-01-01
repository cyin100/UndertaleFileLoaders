#todo
#TOPCAKE/REVIVEBRITE
#EVERYBODYWEAPON
#DEALMAKER (ch2) JEVILSTAIL (ch1)

#BUTTERSCOTCH PIE
#REALKNIFE
#THELOCKET

USERNAME = 'conne'
HACK = 'snowgrave'
WRITETO = 'BACKUP\\filech2_0'

gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\UNDERTALE\\file0'
gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\DELTARUNE\\filech1_0'
gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\DELTARUNE\\filech2_0'

copy = 'DELTARUNE\\snowgrave_ending\\filech2_0'


if HACK == 'snowgrave':
    lowerBound = 264
    upperBound = 325
    


with open(copy, 'r') as file:
    hacked_data = file.readlines()
with open(WRITETO, 'r') as file:
    data = file.readlines()
for line in range(lowerBound, upperBound):
    data[line] = hacked_data[line]
with open(WRITETO, 'w') as file:
    file.writelines(data)