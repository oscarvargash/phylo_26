# Week four: DNA alignments and loops

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

## Cancel a running process

Sometimes an unwanted process happens in our terminal, perhaps we `cat` a really long file or we just insert a typo in the command line. We can simulate an unwanted process by just typing:

```
cat
```

You might think that the terminal is stuck, that we might have missed and argument for `cat`, but `cat`  is operating nevertheless. We can easily cancel the process by typing:

<kbd>control</kbd> + <kbd>c</kbd>

The process is canceled and the terminal is ready to receive a command.

## Aligning DNA matrices

Now that we have been able assemble a DNA regions we can aling those using aligning tools. There are many tools out there to perform aligments, today we will we use mafft.

### Download data

Make a folder for this week:

```
cd Documents
mkdir week_04
cd week_04
```

Download data from genbank:

[https://www.ncbi.nlm.nih.gov/genbank/](https://www.ncbi.nlm.nih.gov/genbank/)

In the search bar type:

```
Diplostephium internal transcribed spacer
```

Select the first 10 results, then download the data:

1. Click on `send to` at the top right
2. Select the `file` option
3. Select the `fasta` format
4. Click on `create file`
5. Select `save file`
6. move the file to `week_04` from `Downloads`

```
mv ~/Downloads/sequence.fasta .
cat sequence.fasta
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Vizualizing and creating alignments

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

We can vizualize the fasta file that we downloaded with `aliview`

```
aliview sequence.fasta 
```

A new windown has been opened, here you can navigate this matrix that has not been aligned. Close the program when you are done and return to the terminal.

Let's make an aligment of for this matrix. We sill use `mafft`, which is one of many tools available. [mafft website](https://mafft.cbrc.jp/alignment/software/algorithms/algorithms.html) contains useful information about the types of algoriths emplyed in the program, and how they compare to other software.

Because we have only have 10 sequences, we will use a computational expensive algorith:

```
mafft --maxiterate 1000 --localpair sequence.fasta > sequence.al.fasta 
aliview sequence.al.fasta
```
Congratulations, you have created your first alignment!

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Loops in bash

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

We can perform iterative actions in bash easily. An interative action is an action that is perfomed in multiple items. For example we can align 10 files with mafft using a single line of code. 

Download the data and unzip it

```
wget https://github.com/oscarvargash/biol_550_2024/raw/main/week_04/files/files_4.zip
unzip files_4.zip
```

We see numerous aligments, we can aling all the files using a loop:

First we should try a simple loop that will call the files we want, this is only for testiing purposes:

```
for file in *g.fasta; do echo $file; done
```

In the code above `file` takes the value of evey item called by `*g.fasta`  in the first set of instructions that end on `;`. The following part of the code performs the action on the item `file`; in this case `echo` simply prints every item. We see that the `file` takes the value of the name of the file.

We can now write a loop that uses mafft to align every item. 

```
for file in *g.fasta; do mafft $file > $file.al; done
```

Beautifully powerful, don't you think?

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Trimming alignments 

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

Let's look at the first aligment:

```
aliview cluster1098_supercontig.fasta.al
```

How does it look?

We can get rid of problematic sections by using a trimmer.

For a single file we can use:

```
trimal -in cluster1098_supercontig.fasta.al -out cluster1098_supercontig.fasta.al.trm -automated1

aliview cluster1098_supercontig.fasta.al.trm 
```

How does it look now?


> Remove your flag if you are good to continue ![](img/green.jpeg)

### Exercise

1. Write a bash loop that trims all alignments from problematic regions.

2. Find the help menu of `TrimAl` and based on examples 6 and 7 at the end of the menu, answer the following question: what other actions can `TrimAl` perform to matrices?


