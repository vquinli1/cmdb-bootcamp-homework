#!/usr/bin/env python

#decided to convert the gtf file to FASTA first. gtf format gives start and end in columns 4 and 5, but not total transcript length.

#/Users/cmdb/data/fastq/cufflinks_out-day1 $ gtf_to_fasta ~/data/fastq/cufflinks_out-day1/transcripts.gtf ~/data/genomes/dmel-all-chromosome-r5.57.fasta ~/data/day3/homework/transcripts.fa

#grep "^>" transcripts.fa | less -S |wc
    #Got 33,890 transcripts (i.e., lines starting with >, each of which is a header for a transcript)

#Next, need to make it so every transcript appears with its header on a single line. Used the fasta parser made this morning, as is:
#../parse_fasta.py < transcripts.fa|less -S

# Plan:
    #Problem is that sequence doesn't start at the same index in every line if both commas and whitespace are delimiters. If whitespace is the only delimiter considered then the sequence starts at position 4.
        #1. Try using strip to retain only indices 2 (the flybase ID) and 4 (the sequence)
        #or
        #2. Sort by length of the string in index 4 (use pandas)
        #3. Take head -n100
        
#To sort:
    def sort_key(item):
        return len(item [1])
    
    longest = sorted(reader, key = sort_key)
    print longest
    
    #Plan for translation:
        #Use a loop. Go through items in the list of tuples generated by 100_longest_final.py, one tuple at a time.
        #Generate revcomp for each sequence and add it back to the tuple as a third item.
        #Go through items in the list of new (3-item) tuples again. For the second and third items, translate 3 times starting at position 1, then 2, then 3. Output all translations to a single list(append).
        
        
        


        