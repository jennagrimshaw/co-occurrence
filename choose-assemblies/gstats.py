#########################################################
# Steps
#########################################################

# 1. Load modules
# 2. Open genome
# 3. Statistics?
#       - Number of reads
#       - Max read length
#       - Min read length
#       - Mean read length
#       - L50
#       - N50

#########################################################
# Load modules
#########################################################
from Bio import SeqIO
import pandas as pd
import statistics as stats
import os
import gzip
print("*** Modules loaded ***")

#########################################################
#  Get list of genomes
#########################################################
genomelist=[]
for file in os.listdir("."):
        if file.endswith(".fa"):
                genomelist.append(file)
print(genomelist)

fields=("Genome", "Total-Length", "Num-of-Records", "Max-length", "Mean-length", "Half", "N50", "L50")
genomestats=pd.DataFrame(columns=fields)

#########################################################
# Get length of all records
#########################################################
TOTLENGTH=[]
NUMREC=[]
MAX=[]
MEAN=[]
L50=[]
N50=[]

for genome in genomelist:
        print(genome)
        BASEPAIRS = []
        for record in SeqIO.parse(genome, "fasta"):
                BASEPAIRS.append(len(record.seq))
        # Calculate basic stats
        TOTLENGTH.append(sum(BASEPAIRS))
        NUMREC.append(len(BASEPAIRS))
        MAX.append(max(BASEPAIRS))
        MEAN.append(stats.mean(BASEPAIRS))
        # Calculate N50
        BASEPAIR_sort=sorted(BASEPAIRS, reverse=True)
        HALF=sum(BASEPAIR_sort)/2
        for counter in range(len(BASEPAIR_sort)+1):
                if sum(BASEPAIR_sort[0:counter])>HALF:
                        L50.append(counter)
                        N50.append(BASEPAIR_sort[counter])
                        print("L50: ", counter)
                        print("N50: ",BASEPAIR_sort[counter])
                        break
print("*** Basic Statistics Calculated ***")
print(TOTLENGTH)
print(NUMREC)
print(MAX)
print(MEAN)

#########################################################
# Population dataframe
#########################################################
genomestats["Genome"] = genomelist
genomestats["Total-Length"] = TOTLENGTH
genomestats["Num-of-Records"] = NUMREC
genomestats["Max-length"] = MAX
genomestats["Mean-length"] = MEAN
genomestats["L50"] = L50
genomestats["N50"] = N50
print(genomestats)

genomestats.to_csv("/lustre/scratch/jenjense/cooc/genomestats.csv", sep=",", index=False)


