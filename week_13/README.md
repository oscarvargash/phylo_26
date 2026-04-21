# Week thirteen: introduction to loops in python

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

## Inspecting fasta-alignment files for length and number of sequences 

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

Now, le's open the file in a text editor, by navigating to it and opening it with the native text editor. It is nice to put the windows next to each other. Copy and paste the following text into our script `name_replacement.py`:

```
#!/usr/bin/python3

import glob
import argparse
import pandas as pd

####### Arguments and help ###########
parser = argparse.ArgumentParser(description="\
Script to change codes to names in files, a translation table is necessary to run the scrip. The translation table should be a comma separated value text file, the first column with the codes to be reaplaced by the names in the second column. Written by Oscar Vargas oscarmvargas.com\
")
parser.add_argument("-i", "--input", help="input file/s ending pattern, required", type=str, required = True)
parser.add_argument("-t", "--translation_table", help="comma separted value table, first column: string to be replaced, second column: replacement, no header")
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

```

> Remove your flag if you are good to continue ![](img/green.jpeg)

Open the script `fasta_descriptor.py` in the text editor next to the terminal window.

![](img/python.png)

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Now we are goint to finish the script adding a loop that interates over every file, and nested on the previous a loop that iterates on each line.

Please add the following code to your script

```
from Bio import SeqIO
```

And add this to the end of the script to test how to count samples in each fasta file and how many sites are present in the aligment, you can remove and/or "comment out" print lines to avoid cluttering your script.

```
print(files)
print(table)
print(dictionary)

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
print("(∩｀-´)⊃/")
print("(∩｀-´)⊃━")
print("(∩｀-´)⊃━☆ﾟ.*･｡ﾟ")
			
```

As you can see, this worked for one single file.

We can now insert this code in the file:

```
for file in fasta_files:
    print(file)
    aln = SeqIO.parse(file, "fasta")   #import alignment
    #print(aln)
    counter = 0                        # create a count from 0
    for seq_record in aln:             # iterate over every seq
        counter +=1
    print(counter)
    seq_len = len(seq_record)         # calculate length
    print(seq_len)     
```

We see that our answer is nicely printed to the terminal, a better way of storing these results would be a table that we can save as a file. The module `pandas` is used for this purpose.

Let's add the modeule to our script at the top of the file:

```
import pandas as pd
```

Now we can add, before the loop, an empty dataframe where we will store the data from the loop

```
print("creating dataframe")
c = ["gene","sequences","length"]
stats = pd.DataFrame(columns=c)
print(stats.head)
```

Now we can add a line in our loop that will populate the dataframe created before the loop. Make sure you add a tab so the code of line so the code is executed in side the loop.

```
stats = stats._append({"gene":file,"sequences":counter,"length":seq_len}, ignore_index=True)
```

When the code is executed, we can see that our results are nicely organized. Finally we just need to save it.

```
stats.to_csv(path_or_buf="gene_stats.csv")
```

Congrats you have created a useful python script!

Do you have any ideas about how to make this script better?

<details>
  <summary>If for any reason you need see the final script, please click here</summary>
  
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# code characterize alignments in fasta

import glob
from Bio import SeqIO
import pandas as pd


fasta_files = (glob.glob)('*.fasta')
print(fasta_files)


print("creating dataframe")
c = ["gene","sequences","length"]
stats = pd.DataFrame(columns=c)
print(stats.head)
        

for file in fasta_files:
    print(file)
    aln = SeqIO.parse(file, "fasta")   #import alignment
    #print(aln)
    counter = 0                        # create a count from 0
    for seq_record in aln:             # iterate over every seq
        counter +=1
    print(counter)
    seq_len = len(seq_record)         # calculate length
    print(seq_len)
    stats = stats._append({"gene":file,"sequences":counter,"length":seq_len}, ignore_index=True)     

stats.to_csv(path_or_buf="gene_stats.csv")

```

> Remove your flag if you are good to continue ![](img/green.jpeg)











