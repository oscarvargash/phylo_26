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
aliview cluster2434_zing.fasta.mafft.oc
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Testing models of evolution in the alignments

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Every DNA region can be modeled using different DNA models of subsitition, we can perform a test in IQtree to infer the best model for each DNA region:

First we can see how iqtree operates:

```
iqtree2
```

Now we can do the analysis and test for a single gene

```
iqtree2 -s cluster2434_zing.fasta.mafft.oc -m MF
cat cluster2434_zing.fasta.mafft.oc.treefile
```

In the output we can see that `iqtree2` perform multiple tests in all the possible models. The [iqtree website](http://www.iqtree.org/doc/) contains useful information for interpreting outputs.

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Performing a Maximum Likelihood tree search

> Add the flag to corner of your screen ![](img/yellow.jpeg)

`iqtree2` is currently the fastest and more accurate program to infer phylogenies using maximum likelihood. It can do the tree search and infer support statistics for the tree at the same time

```
iqtree2 -bb 1000 -s cluster2434_zing.fasta.mafft.oc -redo
cat cluster2434_zing.fasta.mafft.oc.treefile
figtree cluster2434_zing.fasta.mafft.oc.treefile
```

### Quick Exercise

Now that we have inferred one tree, infer another gene tree from the second largest matrix. You will need to look at file sizes to determine which gene to analyze.

<details>
  <summary>Click to see an answer!</summary>
  

```
iqtree2 -bb 1000 -s cluster2784_zing.fasta.mafft.oc
```

</details>

Explore the two trees obtanined, do they represent the same relationships?
*TIP:* to open onther tree in figtree use the drop down file menu from figtree

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Concatenation in iqtree2

iqtree2 can easily run a concatenated analysis without the need to have a supermatrix (which is nice). First we need to put all the alignments in a single folder and then move the alignments there:

```
mkdir concat
mv *.oc ./concat/
```

now we can run the analysis

```
iqtree2 -p ./concat/ --prefix concat_na 1000 -T AUTO
figtree 
```

Now we can see the results

```
figtree concat.treefile
```

### Exercises

1. Look at `concat.best_scheme.nex` using `cat`. What is this?
2. explore other outputs with the prefix `concat.` produce after the analysis (no response is neceseary here, just look at the files and guess their meaning)
3. Open the concatenated tree and compare it with the two gene trees calculated before. Make sure bootstrap support are shown in all three trees. What are the differences between the concatenated tree and the gene trees?
4. Compare the concatenated trees resulted from iqtree and paup. Are they different? explain at least one difference.
5. Calculate bootstrap support using paup. Compare the output with that of iqtree.


```
cd ~/Documents/week_06
paup4a168_ubuntu64
execute supermatrix.nexus
set maxtrees = 1000 increase = no 
bootstrap treefile= bs_all.tree
savetrees file = bs.tree
```

### Optional, loops (this exercise is time consuming for the server)

We can estimate a tree for every single region provided. we can use a loop:

Let's try a simple loop that just print the files we want to analyze:

```
for file in *.co; do echo $file -redo; done
```

We can go one step further and print the commands we want to utilize:

```
for file in *.co; do echo iqtree2 -bb 1000 -s $file -redo; done
```

This looks pretty good, now write the loop in a way that it will analyze every single alignment:

```
for file in *.co; do iqtree2 -bb 1000 -s $file -redo; done
```


### Optional, concatenate "manually"

All the DNA regions in this exercise nuclear genome. In some cases it is best to concatenate all genes in a supermatrix that contains all the phylogenetic signal in a single analysis.

first we need to create a supermatrix using a python3 script that concatenates all the files and creates a partition model. Alternatively you can use [Mesquite](https://www.mesquiteproject.org/Managing%20Molecular%20Data.html#concatMatrices) a program with a graphic interface to perform the concatenation(the use of Mesquite is only advisable when the number of aligments is 5 or less)

```
wget https://github.com/oscarvargash/phylo_26/raw/main/week_07/files/concatenate_all_fasta.py
python3 concatenate_all_fasta.py
```

Let's check the output files

```
aliview supermatrix.fasta
cat supermatrix.model
```

We now can run the supermatrix analysis:

```
iqtree2 -bb 1000 -s supermatrix.fasta -spp supermatrix.model
```

