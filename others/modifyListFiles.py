

import os, sys

#Open a file

path = "/Users/joker/DEV/GAMEs/2-game-BRICKS_MINIMALISTA/export/3/"
dirs = os.listdir( path )

for file in dirs:
    fileName = file
    newFileName = file

    numChar = len( file )
    numCharS = len(file) - 6

    if(file[0:2] == "_0"):
        #print file[0:2]
        newFileName = file[13:numChar]

        comando = "mv " + path + file + " " + path + newFileName
        #print comando
        salida = os.popen(comando).read()
        print("Salida:\n", salida)
    elif(file[numCharS:numCharS + 2] == "4x"):
        newFileName = file[0:numCharS-1]
        #print file
        #print newFileName + ".png"

        comando = "mv " + path + file + " " + path + newFileName + ".png"
        #print comando
        salida = os.popen(comando).read()
        print("Salida:\n", salida)

    else:
        print file
    #print file[12:numChar]

    #print file
