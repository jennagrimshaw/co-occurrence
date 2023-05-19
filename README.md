# co-occurrence

This is a project to analyze co-occurrence patterns in TEs in mammalian genomes.  
I am working with assemblies that have already been generated as well as TE bedfiles

## Step 1. Create directories
- assemblies
- originals
- scripts
- bedfiles

## Step 2. Get data 
Place bedfiles in "originals" directory and assemblies in "assemblies" directory.  I will be filtering the original bedfiles to only include the big 5 (RC, DNA transposons, LINEs, SINEs, & LTRs). I store all my scripts in the "scripts" directory, and then pull them into the main directory while being used and then transfer them back to "scripts".

## Step 3. Choosing assemblies  
I am using two filtering steps: N50 & BUSCO. 
- For N50, run gstats.py in the "assemblies" directory. ** for some reason, the gstats.sh isn't working **
- 
