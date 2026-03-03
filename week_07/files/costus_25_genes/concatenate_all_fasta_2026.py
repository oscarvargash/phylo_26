#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python script to make two kinds of concatenations:
1. a concatenation of introns and exons per gene
2. a supermatrix concatenation
for every concatenation the script produces a RAxML partition
a dataframe is produced with data occupancy per taxon
a summary text with occupancy statistics is produced
"""

import glob
from collections import defaultdict

import pandas as pd
from Bio import AlignIO
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


file_pattern = ".fasta"
all_files = sorted(glob.glob(f"*{file_pattern}*"))

if not all_files:
    raise SystemExit(f"No input files matched pattern '*{file_pattern}*'")

# If you need genes later, keep it as a list in Python 3:
# genes = [fn.split('.')[0] for fn in all_files]


def concatenate(alignments, missing_char="?"):
    """
    Concatenate multiple alignments into a supermatrix.

    Any missing taxa in an alignment are filled with `missing_char` repeated to
    the alignment length.
    """
    # Full set of labels across all alignments
    all_labels = {rec.id for aln in alignments for rec in aln}

    tmp = defaultdict(list)

    for aln in alignments:
        length = aln.get_alignment_length()

        these_labels = {rec.id for rec in aln}
        missing = all_labels - these_labels

        filler = str(Seq(missing_char * length))
        for label in missing:
            tmp[label].append(filler)

        for rec in aln:
            tmp[rec.id].append(str(rec.seq))

    return MultipleSeqAlignment(
        SeqRecord(Seq("".join(parts)), id=label, description="")
        for label, parts in tmp.items()
    )


# Construction of the supermatrix
all_aligns = []
for fn in all_files:
    print(f"reading file {fn}")
    aln = AlignIO.read(fn, format="fasta")
    all_aligns.append(aln)

print("concatenating alignments")
supermatrix = concatenate(all_aligns, missing_char="?")

supermatrix_name = "supermatrix.fasta"
with open(supermatrix_name, "w") as out_handle:
    AlignIO.write(supermatrix, out_handle, "fasta")

print("writing partition file for supermatrix")
lines = []
gene_start = 1
for fn, aln in zip(all_files, all_aligns):
    gene_len = aln.get_alignment_length()
    gene_finish = gene_start + gene_len - 1
    gene_name = fn.split(".")[0]
    lines.append(f"DNA, {gene_name} = {gene_start}-{gene_finish}\n")
    gene_start = gene_finish + 1

model_file_name = "supermatrix.model"
with open(model_file_name, "w") as outfile:
    outfile.writelines(lines)

print("Creating a dataframe summarizing taxon occupancy")
all_labels = sorted(rec.id for rec in supermatrix)

stats = pd.DataFrame(index=all_labels, columns=["number_of_regions", "total_characters"]).fillna(0)
stats.index.name = "sample"

# Count how many regions each taxon appears in
for aln in all_aligns:
    for rec in aln:
        stats.loc[rec.id, "number_of_regions"] += 1

# Count non-missing characters per taxon in the supermatrix
for rec in supermatrix:
    seq_str = str(rec.seq).replace("?", "")
    stats.loc[rec.id, "total_characters"] = len(seq_str)

stats["region_perc"] = stats["number_of_regions"] / len(all_aligns)
stats["characters_perc"] = stats["total_characters"] / supermatrix.get_alignment_length()

stats.to_csv("taxon_occupancy.csv")

print("Calculating matrix occupancy stats")
total_matrix_dimensions = len(supermatrix) * supermatrix.get_alignment_length()
cells_occupied = stats["total_characters"].sum()
cell_occupancy = float(cells_occupied) / float(total_matrix_dimensions)

total_regions = len(supermatrix) * len(all_aligns)
regions_occupied = stats["number_of_regions"].sum()
region_occupancy = float(regions_occupied) / float(total_regions)

with open("occupancy_stats.txt", "w") as outfile:
    outfile.write(
        f"cell occupancy = {cell_occupancy}\n"
        f"region occupancy = {region_occupancy}\n"
    )

print("done (っ▀¯▀)つ")