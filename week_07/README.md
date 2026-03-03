# Week seven: building trees using Maximum Likelihood with iqTree

> Add the flag to corner of your screen ![](img/yellow.jpeg)

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

### Download data

Make a folder for this week:

```
cd Documents
mkdir week_07
cd week_07
```

Download and unzip data from this lab:

```
wget https://github.com/oscarvargash/phylo_26/raw/main/week_07/files/costus_25_genes.zip
unzip costus_25_genes.zip
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Testing models of evolution in the alignments

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Every DNA region can be modeled using different DNA models of subsitition, we can perform a test in IQtree to infer the best model for each DNA region:

First we can see how iqtree operates:

```
iqtree2
```

Now we can do the test for a single gene

```
iqtree2 -s cluster2434_zing.fasta.mafft.oc -m MF
```

In the output we can see that `iqtree2` perform multiple tests in all the possible models. The [iqtree website](http://www.iqtree.org/doc/) contains useful information for interpreting outputs.

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Performing a Maximum Likelihood tree search

> Add the flag to corner of your screen ![](img/yellow.jpeg)

`iqtree2` is currently the fastest and more accurate program to infer phylogenies using maximum likelihood. It can do the tree search and infer support statistics for the tree at the same time

```
iqtree -bb 1000 -s cluster2434_zing.fasta.mafft.oc -redo
figtree cluster2434_zing.fasta.mafft.oc.treefile
```

Let's clean a bit our folder before the next step:

```
rm *.fasta.*
```

Now that we have inferred one tree, we can estimate a tree for every single region provided. we can use a loop:

Let's try a simple loop that just print the files we want to analyze:

```
for file in *.fasta; do echo $file; done
```

We can go one step further and print the commands we want to utilize:

```
for file in *.fasta; do echo iqtree -bb 1000 -s $file; done
```

This looks pretty good, now write the loop in a way that it will analyze every single alignment:

```
for file in *.fasta; do iqtree -bb 1000 -s $file; done
```

Explore the trees obtanined, do they represent the same relationships?

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Runing a supermatrix analysis

> Add the flag to corner of your screen ![](img/yellow.jpeg)

All the DNA regions in this exercise belong to the chloroplast genome. Because this region is a single and large piece of DNA that does not perform recombination, it is safe to assume that a single tree underlies the history of all the chloroplast. In cases like this one it is best to concatenate all genes in a supermatrix that contains all the phylogenetic signal in a single analysis.

first we need to create a supermatrix using a python3 script that concatenates all the files and creates a partition model. Alternatively you can use [Mesquite](https://www.mesquiteproject.org/Managing%20Molecular%20Data.html#concatMatrices) a program with a graphic interface to perform the concatenation(the use of Mesquite is only advisable when the number of aligments is 5 or less)

```
python3 concatenate_all_fasta.py
```

Let's check the output files

```
aliview supermatrix.fasta
cat supermatrix.model
```

We now can run the supermatrix analysis:

```
iqtree -bb 1000 -s supermatrix.fasta -spp supermatrix.model 
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Exercise

Open the concatenated tree `supermatrix.model.treefile` and compare it with two gene trees. Make sure bootstrap support are shown in all three trees. What are the differences between the concatenated tree and the gene trees?

Type your answer in the canvas exercise for this lab.
