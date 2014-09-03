#!/usr/bin/env python

#1. count number of alignments
# location of sam file to use: Users/cmdb/data/fastq/tophat_out-day1/accepted_hits.sam. Copied to data/day2/accepted_hits.sam

tophat_output_fname = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(tophat_output_fname)
total = 0
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    #if "SRR" in line and i>0: This gives a number one larger than it should because one of the header lines contains "SRR"
    if line.startswith("SRR") and i>0:
        total = total + 1
print total #got 18417195 for this data set, checked with grep

#2. count number of perfect alignments

tophat_output_fname = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(tophat_output_fname)
total = 0
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if "NM:i:0" in line and i>0: #Found at http://biobits.org/samtools_primer.html: in the NM field this value indicates a perfect match. No other fields expected to include this string.
        total = total + 1
print total #got 14079052 for this data set

#3. Count number of reads that map to exactly one location in genome. 

tophat_output_fname = "/Users/cmdb/data/day2/accepted_hits.sam"

f = open(tophat_output_fname)
total = 0
for i, line in enumerate(f):
    fields = line.rstrip("\r\n").split("\t")
    if "NH:i:1" in line and i>0: #NH gives the number of hits for the read. This counts reads with 1 hit.
        total = total + 1
print total #got 17444398 for this data set
