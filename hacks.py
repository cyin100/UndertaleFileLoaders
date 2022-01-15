# TODO
# TOPCAKE/REVIVEBRITE
# EVERYBODYWEAPON
# DEALMAKER (ch2) JEVILSTAIL (ch1)

# BUTTERSCOTCH PIE
# REALKNIFE
# THELOCKET

def hackFile(copy, paste):
    with open(copy, 'r') as file:
        hacked_data = file.readlines()
    with open(paste, 'r') as file:
        data = file.readlines()
    for line in range(bounds[0], bounds[1]):
        data[line] = hacked_data[line]
    with open(paste, 'w') as file:
        file.writelines(data)

USERNAME = 'conne'
GAME = 'UNDERTALE'  
HACK = 'butterscotch'

if GAME == 'UNDERTALE':
    gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\UNDERTALE\\file0'

if GAME == 'DELTARUNE_1':
    gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\DELTARUNE\\filech1_0'

if GAME == 'DELTARUNE_2':
    gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\DELTARUNE\\filech2_0'

hackedFile = 'HACKED\\'+GAME

if HACK == 'snowgrave':
    hackFile(gameFile)

if HACK == 'butterscotch':


