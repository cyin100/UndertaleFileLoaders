import subprocess, os

def moveFile(readFile, writeFile):
    try:
        inputFile = open(readFile, 'r')
        outputFile = open(writeFile, 'w')
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

def clearFiles(file):
    if os.path.exists(file):
        os.remove(file)

print('\nUNDERTALE/DELTARUNE File Loader\n')

USERNAME = input('PC Username: ')
NAME = input('IGN: ')  
GAME = input('Game: ')
MODE = int(input('Mode: '))
if MODE == 0:
    LOAD = input('Load: ')

print('\nStarting game...\n')

if MODE == 1:
    for file in os.listdir('BACKUP'):
        clearFiles('BACKUP\\'+file)

if GAME == 'UNDERTALE':
    files = ['undertale.ini', 'file0', 'file8', 'file9']
if GAME == 'DELTARUNE':
    files = ['dr.ini', 'filech1_0', 'filech1_3', 'filech1_9', 'filech2_0', 'filech2_9', 'keyconfig_0.ini']

for file in files:

    selectFile = GAME+'\\'+LOAD+'\\'+file
    backupFile = 'BACKUP\\'+file
    gameFile = 'C:\\Users\\'+USERNAME+'\\AppData\\Local\\'+GAME+'\\'+file

    if MODE == 0:
        clearFiles(gameFile)
        moveFile(selectFile, gameFile)

    if MODE == 1:
        moveFile(gameFile, backupFile)

    if MODE == 2:
        clearFiles(gameFile)
        moveFile(backupFile, gameFile)     

if MODE != 2:
    if GAME == 'UNDERTALE':
        subprocess.Popen('C:\\Program Files (x86)\\Steam\\steamapps\\common\\Undertale\\UNDERTALE')
    if GAME == 'DELTARUNE':
        subprocess.Popen('C:\\Program Files (x86)\\Steam\\steamapps\\common\\DELTARUNEdemo\\DELTARUNE')