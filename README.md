# ListeFichiersDossiersColler
> **_Welcome to the ListeFichiersDossiersColler Wiki!_**



**1. ListeFichiersDossiersColler** : scan a folder to copy and paste names into a notepad The ListFilesFoldersPaste.py script is designed to help you extract file and folder names from a specified folder and save them in a format that can be easily used in Python. Here's how it works:

**2. Creating the start.bat file** : To run this script more easily, you can create a start.bat file containing the command to run the Python script. Make sure that the file ListFilesPaste.py is in the same directory as the start.bat file.

**3. Running the script** : When you double-click on the start.bat file, a terminal window will open and ask you to enter the path to the folder you wish to examine. For example, if you have your files in `C:\MonDossier`, you would enter `C:\MonDossier` (make sure you use backslashes `\` and not slashes `/` for paths on Windows).

Collect file and folder names: The script will browse the folder you've specified and collect the names of all the files and folders it contains.

**4. Formatting for Python** : The names collected will be formatted so that they can be used directly in a Python list. Names will be enclosed in double quotation marks and separated by commas, as in the example `search_a_names = ["file1", "folder1", "file2"]`.

**5. Creation of an output file** : The script will write this formatted list to a text file called here.txt in the same directory as the script. You can change the name of the output file by modifying the path_bloc_notes variable in the script.

Automatic notepad opening: The script will automatically open the here.txt file in your system's default notepad, so you can view the file and folder names you've extracted.

Automatic terminal closing: After displaying file and folder names in the notepad, the terminal will automatically close after a 2-second pause. You can adjust this delay if required.

Use this script to quickly extract and format file and folder names in a specified folder, which can be handy for various programming or organizational tasks.

***

**ListeFichiersDossiersColler - Personal Use License**

Version 1.0, [22/08/2023]

Copyright Light Zirconite

Permission is hereby granted, free of charge, to any person obtaining a copy
of this script and associated documentation files (the "Script"), to use
the Script without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Script, and to permit persons to whom the Script is furnished to do so,
subject to the following conditions:

The Script or a significant portion of it must not be redistributed, published,
or made publicly available without the explicit and written permission of Light Zirconite.

THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SCRIPT
OR THE USE OR OTHER DEALINGS IN THE SCRIPT.

For inquiries regarding permission to redistribute this script, please contact me Discord : lightzirconite

***

[Download V1](https://github.com/LightZirconite/ListeFichiersDossiersColler/releases/tag/python)
