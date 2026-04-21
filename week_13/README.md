# Week thirteen: loops and arguments in python

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

## Creating a script with arguments for flexibility 

> Add the flag to corner of your screen ![](img/yellow.jpeg)

We will work on a new folder called `week_13`. Open a terminal and navigate to `week-12` folder
  
```
cd Documents
mkdir week_13
cd week_13
wget https://github.com/oscarvargash/phylo_26/raw/main/week_13/files/files.zip
unzip files.zip
```

Now let;s make sure we have all the packages we need for our python script.


```
pip install argparse
pip install pandas
```

start a new script that will look into all fasta files in a folder to summarize their contents, let's create an empty text file:

```
touch name_replacement.py
```

Now, le's open the file in a text editor, by navigating to it and opening it with the native text editor. It is nice to put the windows next to each other. 

Open the script `name_replacement.py` in the text editor next to the terminal window.

![](img/python.png)

Copy and paste the following text into our script `name_replacement.py`:

```
#!/usr/bin/python3

import glob
import argparse
import pandas as pd
import time

####### Arguments and help ###########
parser = argparse.ArgumentParser(description="\
Script to change codes to names in files, a translation table is necessary to run the scrip. The translation table should be a comma separated value text file, the first column with the codes to be reaplaced by the names in the second column. Written by Oscar Vargas oscarmvargas.com\
")
parser.add_argument("-i", "--input", help="input file/s ending pattern, required", type=str, required = True)
parser.add_argument("-t", "--translation_table", help="comma separted value table, first column: string to be replaced, second column: replacement, no header. Required")
parser.add_argument("-o", "--output_suffix", help="suffix to be added to output file", type=str, default=".rn")
parser.parse_args()
args = parser.parse_args()


file_suffix = args.input
dict_file = args.translation_table
output_suffix = args.output_suffix
######################################

files = glob.glob("*" + file_suffix)
table = pd.read_csv(dict_file, header = None)
dictionary = dict(table.values)

print(files)
print(table)
print(dictionary)

```

First we can print the help by:

```
python3 name_replacement.py -h
```

We can now execute what we have of the script by adding the required arguments:

```
python3 name_replacement.py -i concat.tree -t clarkia_codes.txt
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

Now we are goint to finish the script adding a loop that interates over every file, and nested on the previous a loop that iterates on each line.

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Please add the following code to your script


```
for file in files:
    print ("working on", file)
    lines = []        
    with open(file) as infile:
        for line in infile:
            for code, name in dictionary.items():
                line = line.replace(code, name)
                print(code, name)
            lines.append(line)
    outfile = file + output_suffix
    with open(outfile, 'w') as outfile:
        for line in lines:
            outfile.write(line)

print("finished")
print("(∩｀-´)⊃/", end="\r")
time.sleep(1)
print("(∩｀-´)⊃━", end="\r")
time.sleep(1)
print("(∩｀-´)⊃━☆ﾟ.*･｡ﾟ")
		
```

Congratulations, you have written your first script with arguments.

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Excercise
Answer the following question:
Would this script work on a fasta file? Please explain your answer carefully indicating why.

