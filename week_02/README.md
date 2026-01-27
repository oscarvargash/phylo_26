# Week two

#### explanation of previous excersise, seq counter
#### explanation of next generation sequencing

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

To start this tutorial you need to be logged in the Linux virtual machine
[vlinux.humboldt.edu](https://vlinux.humboldt.edu/)

Once logged in the Linux machine, look for the Terminal, it is an icon that contains the characters '>\_'

You can also write 'terminal' in the search bar of the main manu located in the left bottom of the operating system.

## Using programs

The terminal is a powerful to run programs, as you can analyze tons of data with only a single command. In this tutorial we will run several aplpications in the terminal and will learn the principles of automatizing data processing.

### Downloading data and initial screening of files

Before analysing the quality of the sequences we need to undertand the basics of [next-generation-sequencing](https://www.youtube.com/watch?v=fCd6B5HRaZ8)

We will use FastQC quatify measure the quality of data in a file.
Please download in your machine a compressed file with the data in a folder named `week_02`:

```
cd Documents
mkdir week_02
cd week_02
wget https://github.com/oscarvargash/phylo_26/raw/main/week_02/files/reads1.zip
```

As you can see, this is a compressed file. We can decompressed by

```
unzip reads1.zip
ls
ls -lh *.gz
```

We can remove now the `.zip` file. How can we remove this files from our folder?

<details>
  <summary>Click to see an answer!</summary>
  
```
rm *.zip
```

</details>


We can try to get peek in the in the file to see what it is about. Print to the screen the first ten lines of the file by typing using the command `head`:

```
head S1870_L008_R1_001.fastq.gz
```

What did you see?

It turns out that this is also a compressed file. `*.gz` is a common type of compression use in DNA analysis. Most bioinformatic programs can work with `*.gz` files, saving space in hard drives. We can look at the file without decompressing it by:

```
zcat S1870_L008_R1_001.fastq.gz | head
```

As you can see we are "piping" or passing with `|` the uncompressed text to `head`, which prints only the first ten lines of the file

What is this file?

### Exercise

Count the number of reads found in each file. Please use wild cards `*`

<details>
  <summary>ONLY AS A LAST RESOURCE (in case you are feeling lost), Click here to see the commands to analyze the data of this exercise</summary>

```
zcat *.gz | grep -c "@"
```

### Using FastQC


We can use FastQC to evaluate the quality of the file. First should figure out how does FastQC works. Most programs have a help menu.




```
fastqc -help
``` 

It seems that we can simply add the name of the file as as the first argument, and we then add `-o` (output) to specify where the program should write the report

```
fastqc S1870_L008_R1_001.fastq.gz -o .
``` 

Once it has finish you can list all files and see the output. 

```
ls
```

Open the file in firefox using the the right clik option "open with." Scroll through the results, for the purposes of this lab we will only pay attention to the "basic statistics" and the "per base sequence quality."  

Congrats!!! you have excuted a program succesfully

### Exercise

Analyze the second file with FastQC. Upon completion of the analysis compare the results (basic statistics and per base sequence quality) and decide which of the files contains better data in terms of quality. Submit your answer in CANVAS along with a brief explanation.

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Triming and cleaning reads

> Add the flag to the corner of your screen ![](img/yellow.jpeg)

We will trim the reads found in the files from contaminants and low quality regions. We will use a suite of programs called `bbtools`, specifically we will use the program `bbduk.sh`. Let's call the program and see the help:

```
bbduk.sh -h
```

We want to trim contaminants found in the reference file `adapters.fa`. Let's take a look at the file 

```
cat ~/../../opt/bbmap/resources/adapters.fa
```

Now run bbduk:

```
bbduk.sh in=S1870_L008_R1_001.fastq.gz ref=~/../../opt/bbmap/resources/adapters.fa ktrim=r k=21 mink=11 hdist=2 ml=50 out=S1870_L008_R1_001.f.fastq.gz stats=statsf1.txt
```

`ktrim` indicates which side of the read should be trimmed

`k` indicates the kmer size to look for contaminats, contaminants shorther than K will not be found

`mink` looks for shorter kmers at the end of reads

`hdist` indicates the number of mistmatches allowed in the kmer for matching to contaminants

`ml` is the minimum lenght of a given read

Now that we have removed contaminants we will remove regions of the reads with low quality scores

```
bbduk.sh in=S1870_L008_R1_001.f.fastq.gz ref=~/../../opt/bbmap/resources/adapters.fa qtrim=lr trimq=20 minlength=21 out=S1870_L008_R1_001.ft.fastq.gz stats=statst1.txt
```

`qtrim` indicates where to trim reads, in this case we are triming on both left and right

`trimq` indicates the minimum phred score allowed

`minlength` indicates the minimum lenght of a read allowed

> Remove your flag if you are good to continue ![](img/green.jpeg)

### Exercise

Perform the filtering and trimming in the second file `*R2*`. Make sure the file name for the stats is different. Answer the following questions and submit your answers to CANVAS:

1. Which file had more contaminants R1 or R2 (`statsf*`)?

2. Was there a significant difference in the trimming between R1 and R2 (`statst*`)? briefly explain


<details>
  <summary>ONLY AS A LAST RESOURCE (in case you are feeling lost), Click here to see the commands to analyze the data of this exercise</summary>
  
```
bbduk.sh in=S1870_L008_R2_001.fastq.gz ref=~/../../opt/bbmap/resources/adapters.fa ktrim=r k=21 mink=11 hdist=2 ml=50 out=S1870_L008_R2_001.f.fastq.gz stats=statsf2.txt

bbduk.sh in=S1870_L008_R2_001.f.fastq.gz ref=~/../../opt/bbmap/resources/adapters.fa qtrim=lr trimq=20 minlength=21 out=S1870_L008_R2_001.ft.fastq.gz stats=statst2.txt


fastqc S1870_L008_R1_001.ft.fastq.gz -o .
fastqc S1870_L008_R2_001.ft.fastq.gz -o .
```

</details>

