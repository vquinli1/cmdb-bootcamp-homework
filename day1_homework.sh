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
