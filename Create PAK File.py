from tkinter import Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilenames
import zlib, os
tk = Tk()
tk.iconbitmap(default='icon.ico')
tk.withdraw()
filesPath = askopenfilenames(title='Select Files')
if not len(filesPath)==0:
    inputFileCount = int(len(filesPath))
    inputFiles = []

    outputFile = open('OUTPUT.PAK','wb+')

    fileOffsets = []
    fileSizes = []
    fileNameOffsets = []

    for i in range(inputFileCount):
        inputFiles.append(filesPath[i])

    outputFile.write(inputFileCount.to_bytes(4, 'little'))
    outputFile.write(b'\x00'*(inputFileCount*12))

    for i in range(inputFileCount):
        fileNameOffsets.append(outputFile.tell())
        outputFile.write(os.path.basename(inputFiles[i]).encode('utf8')+b'\x0A\x00')

    for i in range(inputFileCount):
        inputFile = open(inputFiles[i],'rb+')
        compressedFile = zlib.compress(inputFile.read())
        fileOffsets.append(outputFile.tell())
        fileSizes.append(len(compressedFile))
        outputFile.write(compressedFile)

    outputFile.seek(4)
    for i in range(inputFileCount):
        outputFile.write(fileOffsets[i].to_bytes(4, 'little'))
        outputFile.write(fileSizes[i].to_bytes(4, 'little'))

    for i in range(inputFileCount):
        outputFile.write(fileNameOffsets[i].to_bytes(4, 'little'))