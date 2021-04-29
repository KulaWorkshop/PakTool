import sys, zlib, os

class compressedFile:
    offset = 0
    size = 0
    nameOffset = 0

compressedFiles = []

try:
    pakFile = open(sys.argv[1],'rb+')

    compressedFileCount = int.from_bytes(pakFile.read(4),'little')
    for i in range(compressedFileCount):
        currentFile = compressedFile()
        currentFile.offset = int.from_bytes(pakFile.read(4),'little')
        currentFile.size = int.from_bytes(pakFile.read(4),'little')
        compressedFiles.append(currentFile)

    for i in range(compressedFileCount):
        currentFile = compressedFiles[i]
        currentFile.nameOffset = int.from_bytes(pakFile.read(4),'little')

    if not os.path.isdir(sys.argv[1].split('.')[0]): os.mkdir(os.path.basename(sys.argv[1]).split('.')[0]) 

    for i in range(compressedFileCount):
        currentFile = compressedFiles[i]
        pakFile.seek(currentFile.nameOffset,0)
        fileName = ''
        while True:
            character = pakFile.read(1)
            if character==b'\x0A'or character==b'\x00':break
            else:fileName+=character.decode('ascii')
        pakFile.seek(currentFile.offset,0)
        open(os.path.basename(sys.argv[1]).split('.')[0]+'/'+str(fileName),'wb').write(zlib.decompress(pakFile.read(currentFile.size)))
except: pass