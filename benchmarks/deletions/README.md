# Deletions
Only two of the GIAB samples currently have released deletion datasets.
Neither of these datasets are available in hg38, so they were lifted over semi-manually to create the truth sets.

## HG001
The HG001 benchmark is derived from the [paper for svclassify](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-016-2366-2) and contains 2676 deletions events.
To our knowledge, this is the precursor to offical GIAB SV/CNV benchmarks.
However, it is not currently listed on the GIAB website.

Steps to generate hg38 benchmark file:
1. Download the bed file containing the deletions from the [supplementary material for the paper](https://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/technical/svclassify_Manuscript/Supplementary_Information/Personalis_1000_Genomes_deduplicated_deletions.bed).
2. Manually liftover the bed file from hg19 to hg38 using the UCSC liftover tool: [https://genome.ucsc.edu/cgi-bin/hgLiftOver](https://genome.ucsc.edu/cgi-bin/hgLiftOver)
3. Use `SURVIVOR bedtovcf` to generate VCF body info.
4. Mock header information and replace genotype calls with "0/1" inside the VCF. 
5. Sort, `bgzip`, and `tabix` the result.
6. For ease of comparison, we have uploaded the final hg38 VCF file to this repo.

## HG002
The HG002 benchmark is derived from the [GIAB v0.6 release](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/analysis/NIST_SVs_Integration_v0.6/) and restricted to deletions.

Steps to generate hg38 benchmark file:
1. Download the [VCF file from GIAB](https://ftp-trace.ncbi.nlm.nih.gov/ReferenceSamples/giab/data/AshkenazimTrio/analysis/NIST_SVs_Integration_v0.6/HG002_SVs_Tier1_v0.6.vcf.gz).
2. We wrote a script to convert only the deletions calls from the VCF file into a BED file.
3. Manually liftover the bed file from hg19 to hg38 using the UCSC liftover tool: [https://genome.ucsc.edu/cgi-bin/hgLiftOver](https://genome.ucsc.edu/cgi-bin/hgLiftOver)
4. Use `SURVIVOR bedtovcf` to generate VCF body info.
5. Mock header information and replace genotype calls with "0/1" inside the VCF. 
6. Sort, `bgzip`, and `tabix` the result.
7. For ease of comparison, we have uploaded the final hg38 VCF file to this repo.

## Important Caveats
1. Both deletion benchmarks were originally created in hg19.  It is possible that liftover of the variant leads to incorrect events in the benchmark file due to imprecision from the coordinate conversion. Ideally, these benchmarks will be generated for hg38 in the future.
2. The HG001 benchmark does not have "high-confidence" or "benchmark" regions provided with the dataset. As a result, we are *ignoring* the region file provided for HG002.  This means that precision is effectively a *lower-bound* on precision, and does *NOT* reflect the performance of the tools in well-behaved benchmark regions.  This may change in the future as benchmarks are improved.
