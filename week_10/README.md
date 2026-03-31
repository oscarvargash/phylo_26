# Week ten: coalescent analysis using Astral

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

## creating a coalescent-consistent tree

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Let's download the data needed for this week's tutorial

```
cd Documents
mkdir week_10
cd week_10
wget https://github.com/oscarvargash/phylo_26/raw/main/week_10/files/files.zip
unzip files.zip
```

### Inferring gene trees

We first need to infer gene trees for each on the genes in the downloaded data. Notice that we will use GTR+G to save some time from model testing.

```
for file in *.aln-cln; do iqtree2 -bb 1000 -s $file -m GTR+G; done
```

Let's take a look at one tree:

```
cat AT5G37830.names.fa.aln-cln.treefile
```

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Building a coalescent consistent species tree

> Add the flag to corner of your screen ![](img/yellow.jpeg)

The first step for using Astral-pro3 is to create a single file that contains all the trees. To create a single tree we can use `cat` and a wildcards in the following way:

```
cat *cln.treefile > nc_20g.tre
```

Let's check that the concatenation of tree files worked:

```
cat nc_20g.tre
```

We can now run Astral-pro3:

```
./astral-pro3 -i nc_20g.tre -o nc_astral.tre
```

We can now see the tree in fig tree:

```
figtree nc_astral.tre
```

Super-Mega-Congrats you have created your first coaslescent-consistent phylogenetic tree

> Remove your flag if you are good to continue ![](img/green.jpeg)


