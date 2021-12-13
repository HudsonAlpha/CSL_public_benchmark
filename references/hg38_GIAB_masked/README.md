# hg38_GIAB_masked
This reference is a masked version of the hg38 reference genome released by various members of the [Genome in a Bottle](https://www.nist.gov/programs-projects/genome-bottle) and [Telomere-to-Telomere (T2T)](https://sites.google.com/ucsc.edu/t2tworkinggroup) Consortiums.
Briefly, the reference is an attempt to recover some of the benefits of the CHM13 reference genome released by T2T without a change in coordinate system.
It removes some false duplications from the reference by masking (e.g. changed to 'N's) the duplications without shifting the sequences at all.
It includes all of the primary contigs along with the "_random" and unplaced contigs from hg38.
For more information, review [this preprint, "Towards a Comprehensive Variation Benchmark for
Challenging Medically-Relevant Autosomal Genes"](https://www.biorxiv.org/content/10.1101/2021.06.07.444885v3), by various members of GIAB and the T2T consortium.

A direct link to the reference file is included in `get_ref.sh`.
The reference genome itself was unaltered for our processing.
The ALT contig file included in this repository is a dummy file that was created for systematic processing in the pipelines.
