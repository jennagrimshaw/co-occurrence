## Gstats for N50
This is a python script that uses several packages namely: os, pandas, and Bio. 
To install these packages in your environment (if using bash on HPCC) use conda

    conda install os
  
## BUSCO
I created a dedicated environment for using busco which assesses assembly completeness.  I did have some issues with busco installation so i got help from our HPCC support. And it did take a long time but it did work. 

    conda config --remove channels conda-forge
    conda config --add channels conda-forge
    conda update conda  #this took awhile
    conda activate busco
    conda install -c conda-forge -c bioconda busco=5.4.7 #this took a long time including several "failed to solve" but it eventually did i

  
