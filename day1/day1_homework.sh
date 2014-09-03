#!/bin/bash

#
# Day 1 - Homework: Part 2 - debug this bash script
#

FASTQ_DIR=/Users/cmdb/data/fastq
#not currently using this variable 
FASTQC_OUTPUT=/Users/cmdb/data/day1/SRR072_fastqc_output
TOPHAT_OUTPUT_DIR=/Users/cmdb/data/day1/SRR072_tophat_output
#removed "=" in middle of file path, renameds specific to tophat
CUFFLINKS_OUTPUT_DIR=/Users/cmdb/data/day1/SRR072_cufflinks_output
#created new variable for cufflinks output (could send to the same place, but assuming this should be able to send the tophat output to cufflinks)
GENOME_DIR=/Users/cmdb/data/genomes/dmel5
#removed "=" in middle of file path
ANNOTATION=~/data/day1/lunch/dmel-all-r5.57.gff
#added additional file path information
CORES=4
#set value to 4, added this to the script below
FILES=/Users/cmdb/data/day1/test/*
#made a folder of placeholder files: text files named TEST1 copy 1-24.rtf
BAM_FILES=/Users/cmdb/data/day1/SRR072_tophat_output/*.bam

for read in $FILES
do
  echo fastqc $read -o $FASTQC_OUTPUT
  echo tophat -p $CORES -G $ANNOTATION -o $TOPHAT_OUTPUT_DIR --no-novel-juncs --segment-length 20 $GENOME_DIR $read
done
for bamfile in $BAM_FILES
do
  echo cufflinks -p $CORES -G $ANNOTATION -o $CUFFLINKS_OUTPUT_DIR $bamfile
done

#other way to specify that it goes through 24 files, closer to the original:

#for the input, $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz. Next 2 are $OUTPUT_DIR/similar pattern. To run for a series of file endings, use "for i in {893..916}" Sample prefix is what is same in every file name, only last 3 numbers vary and are a series.
#"\." means that there is a dot after the variable i. (i.e., ends the variable) In general, backslash is used to say that a special character (like a $ or .) should literally be used.
#to view results with long lines, after running program do "less -S" to turn off line wrap.
#if fastq data goes to OUTPUT_DIR, then input for tophat is 
#To set output for multiple files, use $OUTPUT_DIR (and set a value for this) and set output to $OUTPUT_DIR/th_$i.
#To generate a list of numbers, use seq command or echo {893..916}
#tail command gives the last 10 (or set number) of a series
#Rather than making completely separate output directories, create subdirectories in #OUTPUT_DIR!

#To download the sequences from the search results page, use the "send to" command on the NCBI website.

#If I run cufflinks as part of the same loop as the other commands I can use "accepted_hits.bam" (with the correct directory specified, specific to "i") as the input file.

#Advanced exercises:
#1.Calculate how many alignments are on each chromosome from a SAM file.
#Use head to look at the line formatting. Can see that the 3rd column is the chromosome number, and that each alignment takes up one line (though it looks like 2 with line wrap on). (head accepted_hits.sam) Use grep "^SRR" accepted_hits.sam | cut -f3 | uniq -c > outputfile.txt
#Selects lines starting with SRR | cuts out column 3 | outputs unique items with counts. To sort the results from uniq use the -n option to sort numerically.

#2. Find position at which most reads start their alignment in a SAM file. 