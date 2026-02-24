# Week five: building trees using PAUP, GitHub

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

### Download data

Make a folder for this week:

```
cd Documents
mkdir week_05
cd week_05
```

Download data from this lab:

```
wget https://github.com/oscarvargash/phylo_26/raw/main/week_06/files/supermatrix.fasta
```

### Exporting the data as a nexus file

So far we have only been working with `*.fasta` files; PAUP, however, does not read fasta files, and instead uses nexus files. We can use aliview to export our matrix to `*.nexus`

```
aliview supermatrix.fasta
```

Then do the following:
1. Click on `file`
2. Click on `save as nexus`
3. Keep the suggested name and `save`
4. Close aliview


How do we know the format has changed?

<details>
  <summary>Click to see an answer!</summary>

```
head supermatrix.nexus
```

</details>

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Using PAUP

Paup can be used as an interactive program or you can write all your commands at the end of a nexus file to perform analysis. Today we will use interactively using one command at a time. To open PAUP simply type:

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

```
paup4a168_ubuntu64
```

You can see that the command line has change and now says `puap>`. You are now inside the PAUP program, and PAUP is waiting for instructions.

Let's see what are our command options:

```
?
```

In PAUP, we first need to open our data matrix:

```
execute supermatrix.nexus
```

You should see a summary of the about the taxa imported.

In order to better make sense of trees produced, we will set the outgroup:

```
outgroup Typha_latifolia
```

Do a parsimony search:

```
hsearch
```

When asked about increasing the number of maximum trees, type `y`, then write `200`, and finally type option `2` to avoid this question in the future. At the end of the search you should see a summary of all the trees found.

We can see a single tree by typing

```
ShowTrees
```

This option shows tree 1 saved in memory. If we want to see another tree we need to know the sintax for `ShowTrees`

```
ShowTrees ?
```

How do we display tree 99?

Because we have more than a 100 trees, a good strategy is to summarize our results into a concensus tree.

```
contree
```

You will realize that the consesus tree has some polytomies, these polytomies indicate inconsistensis of multiple trees that contain the same lenght.

Let's save the tree

```
contree / treefile = par_con.tre
```

Congrats, you have performed your first phylogenetic analysis!!!!!

Let's quit paup

```
quit
```

A better way to vizualize trees is to use figtree

```
figtree par_con.tre
```

Figtree will become your best friend.

> Remove your flag if you are good to continue ![](img/green.jpeg)


### Exercise

Use PAUP and the same data downloaded earlier in this tutorial.

Infer, save, and compare a NeighborJoining `nj` tree against a `upgma` tree. You will need to save every tree after every analysis using `SaveTrees`. 
Are these trees different?

Type your answer in the canvas exercise for this lab.