# Computational laboratory for BIOL 451/551 Phylogenetic Systematics

> **NOTE** 
> This tutorial was developed for a class at Cal Poly Humboldt for the spring of 2026. 
> Some of the material has beed modified from another workshop repository that I co-authored with Merly Escalona at UCSC [Intro to computational tools at UCSC](https://github.com/merlyescalona/ucsc-eeb-intro2comptools) 

The aim of the lab is to provide the skills necessary to analyze data from next-generation sequencing using phylogenetic methods. The analyses are designed so they can be scalable to big data. Students will first learn how to use the command line, then will learn how to use an array of phylogenetic software, and finally will gain some skills in R and python coding.

These tutorials are hands-on and were designed to be followed on a Linux machine with all the software pre-installed. However, a list of software can be found at the bottom of this page for your reference.

## What to expect?

At the end of the course participants will be comfortable using the bash environment, runing phylogentic software, and writing basic python and R scripts.

## Conecting to HSU virtual labs

Every week in lab you will connect to a Linux virtual machine. There are two ways of connecting to the virtual machine:

1. log in with HSU credetials into the [vlinux.humboldt.edu](https://vlinux.humboldt.edu/) This should work smoothly in your computer station at the lab and possibly in your own laptop.

When connected select > Show the remote desktop at its resolution using scroll bars, then > Resize the remote display to match this window

2. Install NoMachine in your laptop. [Installation instructions](https://its.humboldt.edu/vlinux-home-instructions)

## Weekly program (subject to change):

[W-1](https://github.com/oscarvargash/phylo_26/tree/main/week_01) Introduction to bash

[W-2](https://github.com/oscarvargash/phylo_26/tree/main/week_02) Executing programs in bash, FastQC, BBtools: BBDuk

[W-3](https://github.com/oscarvargash/phylo_26/tree/main/week_03) Mapping reads BBmap, IGV, samtools, GenBank

[W-4](https://github.com/oscarvargash/phylo_26/tree/main/week_04) Alignments, mafft, aliview, bash loops

W-5 Project presentations

[W-6](https://github.com/oscarvargash/phylo_26/tree/main/week_06) Paup, TNT, FigTree

[W-7](https://github.com/oscarvargash/phylo_26/tree/main/week_07) IQtree, concatenation

[W-8] Mr. Bayes

[W-9] Bash scripts, Beauti & the Beast

[W-10] Astral-pro3, GitHub

[W-11] Mapping characters

[W-12]Introduction to python

[W-13] Packages and loops in python

# Instructor:

[Oscar Vargas](http://oscarmvargas.com/) (<ov20@humboldt.edu>): botanist and evolutionary biologist, experience with bioinformatics and phylogenomics. Assistant Professor at Humboldt State University.

# Appendix, software used in the tutorials

Here is a list of the software associated with the lab. You do not need to install these in your machine unless you really want to. This software has been installed in the virtual Linux machines of HSU.

[BBtools](https://jgi.doe.gov/data-and-tools/bbtools/bb-tools-user-guide/installation-guide/)

[FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

[SAMtools](http://www.htslib.org/)

[Integrative Genomics Viewer (IGV)](https://software.broadinstitute.org/software/igv/)

[MAFFT](https://mafft.cbrc.jp/alignment/software/)

[TrimAl](http://trimal.cgenomics.org/)

[Mesquite](https://www.mesquiteproject.org/Installation.html)

[AliView](https://ormbunkar.se/aliview/)

[PAUP](https://paup.phylosolutions.com/get-paup/)

[TNT]https://www.lillo.org.ar/phylogeny/tnt/

[IQTREE](http://www.iqtree.org/)

[Figtree](http://tree.bio.ed.ac.uk/software/figtree/)

[BEAST](https://github.com/beast-dev/beast-mcmc)

[Tracer](https://github.com/beast-dev/tracer/releases)

[MrBayes](https://nbisweden.github.io/MrBayes/download.html)

[Astral3-pro](https://github.com/chaoszhang/ASTER/blob/master/tutorial/astral-pro3.md)

Linux programs: git, ssh

Python3 modules: biopython, collections, glob, pandas, numpy, sys, os, re, operator, argparse, gzip, math

R packages: phytools, maps, ape, ggplot2


