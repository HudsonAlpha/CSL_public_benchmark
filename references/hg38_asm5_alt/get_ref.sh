#direct link to the public resource
wget https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Homo_sapiens_assembly38.fasta
ln -s Homo_sapiens_assembly38.fasta hg38.fa
wget https://storage.googleapis.com/genomics-public-data/resources/broad/hg38/v0/Homo_sapiens_assembly38.fasta.64.alt

#the generates our alt contigs
head -n 30882735 ./hg38.fa > hg38_only_main.fa #magic cutoff for primary chromosomes
tail -n +30997795 ./hg38.fa > hg38_only_alt.fa #magic cutoff for the alts
~/githubDL/minimap2-2.17/minimap2 -ax asm5 -r 7000 ./hg38_only_main.fa ./hg38_only_alt.fa > alt_to_main.sam
(cat alt_to_main.sam | grep -v "_decoy"; cat Homo_sapiens_assembly38.fasta.64.alt | grep "_decoy") > hg38.fa.alt

#this step is only for packaging for github
cat hg38.fa.alt | gzip > hg38.fa.alt.gz
