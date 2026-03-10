# Week eight: building trees MrBayes

> Add the flag to corner of your screen ![](img/yellow.jpeg)

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters `>\_`

You can also write `terminal` in the search bar of the main manu located in the left bottom of the operating system.

### Download data

Make a folder for this week:

```
cd Documents
mkdir week_08
cd week_08
```

Download and unzip data from this lab:

```
wget https://github.com/oscarvargash/phylo_26/raw/main/week_08/files/files.zip
unzip files.zip
```

### Preparing the file for MrBayes

Mr.Bayes only works with `nexus` files. Therefore, we need to convert our `fasta` file into a a `nexus` one. We have done this before with `Aliview`:

```
aliview cp_2_genes.fasta
cat cp_2_genes.model
```

In `aliview`:

1. click on the `file` menu
2. `save as` nexus (for Mr. bayes, second nexus option)
3. `save`

MrBayes operates like PAUP, it is a command line program that can operate interactively or with a script. We will use a script today. In order to do so, we need to add the commands for our analysis to the end of our fasta file:

```
xdg-open cp_2_genes.nexus
```

Once the file is open, paste the following text at the bottom of the `nexus` file after removing the block for codons

```
begin mrbayes;

    [This block defines several different character sets that could be used in partitioning these data
    and then defines and enforces a partition called favored.]

    charset ccsA-ndhD = 1-1263;
    charset ycf1and2 = 1264-3709;

    partition favored = 2: ccsA-ndhD, ycf1and2;

    set partition=favored;
    lset app=(1,2) rates=gamma nst=6;
    unlink revmat=(all) shape=(all) statefreq=(all);
    prset applyto=(all) ratepr=variable;
    
    mcmc ngen=500000 printfreq=1000 samplefreq=1000 relburnin=yes burninfrac=0.25							
	diagnfreq=1000 diagnstat=maxstddev											
	nchains=4 savebrlens=yes 
	filename=cp_2_genes;
	sump;
	sumt;

end;

```

Make sure to save the file and then close the editor.

### Running MrBayes

```
mb -i cp_2_genes.nexus
```

This will take some minutes, lets keep the program running while we talk about all the parameters used in this analysis.

Stop the analysis, type `no` when Mr.Bayes ask you if you want to continue with the analysis.

Once the analysis has finished type `quit` to exit MrBayes

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Checking the output

> Add the flag to corner of your screen ![](img/yellow.jpeg)

Let's take a peek of some of these files

```
head cp_2_genes.run1.p
tail cp_2_genes.run1.t
```

What are those files?

We can take a more detailed look at the `*.p` file:

```
tracer
```

Drag and drop the one of the `*.p` files on the  `tracer` application. Summary statistics are shown for every parameter calculated.

Now drop the other `*.p` file. If both chains converged they should present similar likelihood values.

If everything looks good, now you know that you can trust the final result:

```
figtree cp_2_genes.con.tre
```

You will need to turn on the `node labels` and select the appropiate statistic.

Congrats you have performed your first Bayesian phylogenetic analysis,

> Remove your flag if you are good to continue ![](img/green.jpeg)


### Exercises

Please submit all your answers to canvas.

## 1

Do a Maximum Likelihood analysis of `cp_2_genes.fasta` along with `cp_2_genes.model` using `iqtree2`, make sure every gene has a different partition. Compare the Maximum Likelihood tree against the Bayesian tree and answer the following questions:

A. In terms of relationships among the tips. Do both trees have the same relationships? Give specific examples to support your answer.

B. In terms of branch lenghts. Do both trees show similar branch lengths? Give specific examples to support your answer.

C. In terms of support. Do both trees present similar support values? Give specific examples to support your answer and remember that roughly 70% bootstrap corerspond to 0.95 posterior probability.

## 2

Do parsimony analysis using `paup` then compare the parsimony results with those of Mr.Bayes. Make sure to make a consensus tree of all most parsimonious trees obtained.

A. In terms of relationships among the tips. Do both trees have the same relationships? Give specific examples to support your answer.

