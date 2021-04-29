A simple tool that allows for the extraction and creation of custom PAK files for the Kula World games. This tool can be used for compressing custom made levels into a .PAK
file readable by the game's engine. This tool can also be used for extracting levels from the .PAK file so they can viewed and edited easily. For more information on the .PAK file structure, please visit: http://wiki.kulaworkshop.net/index.php/.PAK_Files. This tool currently supports:
  - Kula World
  - Roll Away
  - Kula Quest
  - Most of the Demos

How to Extract PAK Files: Drag and drop the .PAK file onto the "Extract PAK File.exe" or "Extract PAK File.py". A folder will be created in the same directory containing all of the extracted levels from the PAK file.

How to Create PAK Files: Open "Create PAK File.exe" or run "Create PAK File.py", a file dialogue should appear. Select all of the levels in the directory of your choosing, and make sure the order of the files selected in the text box are in the correct order you would like the levels to be loaded. A file called "OUTPUT.PAK" will be created in the same directory containing the compressed level files specified.

**Please Note:** Unfortunately, the compiled executables for the PAK Tool may be detected as a virus. I can assure you this is a false positive. This is an issue with compiling with pyinstaller, and is out of my control.
