import subprocess, os

USERNAME = ''                   # Your PC's username
NAME = 'PLAYER'                 # Your player name
GAME = 'UNDERTALE'              # 'UNDERTALE' or 'DELTARUNE'
SELECTED = 'genocide_sans'      # Selected route
BACKUP = ''                     # '': SELECTED to GAME; 'SAVE': GAME to BACKUP; 'LOAD': BACKUP to GAME;

if GAME == 'UNDERTALE':
    files = ['undertale.ini', 'file0', 'file8', 'file9']
if GAME == 'DELTARUNE':
    files = ['dr.ini', 'filech1_0', 'filech1_3', 'filech1_9', 'filech2_0', 'filech2_9', 'keyconfig_0.ini']

if BACKUP == 'SAVE':
    for file in os.listdir('BACKUP\\'):
        os.remove('BACKUP\\'+file)

for file in files:

    backupFile = 'BACKUP\\'+file
    gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\'+GAME+'\\'+file

    if BACKUP == 'LOAD':
        localFile = backupFile
    else:
        localFile = GAME+'\\'+SELECTED+'\\'+file

    if BACKUP == 'SAVE':
        try:
            inputFile = open(gameFile, 'r')
            outputFile = open(backupFile, 'w')
            data = inputFile.readlines()

            for line in data:
                outputFile.write(line)
        
            inputFile.close()
            outputFile.close()
        except FileNotFoundError:
            pass

    try:
        inputFile = open(localFile, 'r')
        outputFile = open(gameFile, 'w')
        data = inputFile.readlines()

        for line in data:
            if GAME == 'DELTARUNE':
                line = line.replace('RUNE', NAME)
            if GAME == 'UNDERTALE':
                line = line.replace('Rose', NAME)
            outputFile.write(line)

        inputFile.close()
        outputFile.close()
    except FileNotFoundError:
        pass

if BACKUP != 'SAVE':
    if GAME == 'UNDERTALE':
        subprocess.Popen('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale\\UNDERTALE')
    if GAME == 'DELTARUNE':
        subprocess.Popen('C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNEdemo\\DELTARUNE')