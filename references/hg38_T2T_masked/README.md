# hg38_T2T_masked
This *is the second version* of a masked hg38 reference genome released by various members of the [Genome in a Bottle](https://www.nist.gov/programs-projects/genome-bottle) and [Telomere-to-Telomere (T2T)](https://sites.google.com/ucsc.edu/t2tworkinggroup) Consortiums.  The first version is the version labeled `hg38_GIAB_masked` in this repository.

Briefly, the reference is an attempt to recover some of the benefits of the CHM13 reference genome released by T2T without a change in coordinate system.
It removes some false duplications from the reference by masking (e.g. changed to 'N's) the duplications without shifting the sequences at all.
It includes all of the primary contigs along with the "_random" and unplaced contigs from hg38.
For more information, review [this paper, "Curated variation benchmarks for challenging medically relevant autosomal genes"](https://doi.org/10.1038/s41587-021-01158-1).

A direct link to the reference file is included in `get_ref.sh`.
The reference genome itself was unaltered for our processing.
The ALT contig file included in this repository is a dummy file that was created for systematic processing in the pipelines.
