#!/bin/bash
#SBATCH --chdir=./
#SBATCH --job-name=N50
#SBATCH --output=%x.o%j
#SBATCH --error=%x.o%j
#SBATCH --partition nocona
#SBATCH --nodes=1
#SBATCH --ntasks=12
#SBATCH --time=48:00:00
#SBATCH --mail-user=jenna.grimshaw@ttu.edu
#SBATCH --mail-type=ALL

# This script doesn't work... dont know why


echo $(date)


DIRECTORY="/lustre/scratch/jenjense/cooc/assemblies"

cd $DIRECTORY

python /lustre/scratch/jenjense/cooc/gstats.py

echo "It took:"
echo $SECONDS
