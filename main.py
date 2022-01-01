import subprocess

USERNAME = 'conne'                 # Your PC's username
GAME = 'UNDERTALE'                 # 'UNDERTALE' or 'DELTARUNE'
SELECTED = 'pacifist_napstablook'  # 
BACKUP = 'SAVE'                    # 'N/A': SELECTED to GAME; 'SAVE': GAME to BACKUP; 'LOAD': BACKUP to GAME;

if GAME == 'UNDERTALE':
    files = ['undertale.ini', 'file0', 'file8', 'file9']
if GAME == 'DELTARUNE':
    files = ['dr.ini', 'filech1_0', 'filech1_3', 'filech1_9', 'filech2_0', 'filech2_9', 'keyconfig_0.ini']

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