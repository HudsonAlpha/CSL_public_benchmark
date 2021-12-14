# hg38_asm5_alt
Briefly, this reference is a modification of the [GATK Resource Bundle](https://gatk.broadinstitute.org/hc/en-us/articles/360035890811-Resource-bundle)'s reference genome that was released a few years ago.
A direct link to the reference file is included in `get_ref.sh`.
The reference genome itself was unaltered for our processing.

The main change we made was to re-map the alternate (ALT) contigs (thanks to [Erik Garrison](https://twitter.com/erikgarrison/status/1247856824319082496) for suggesting a simple approach to accomplish this goal).
The exact ALT remappings are contained in `hg38.fa.alt`.
Steps for replicating the process from scratch is included in `get_ref.sh`.

The main reason we initially made this change was to recover high-quality mappings in two regions that we cared about clinically:
1. _CYP2D6_ - prior to this ALT change, we were not able to successfully run the [Cyrius](https://github.com/Illumina/Cyrius) tool; after the change, correct haplotype calls were recovered
2. _MAPT_ - prior to this ALT change, mappings in the _MAPT_ gene were frequently low quality due to incorrect handling of multi-mapping; after the change, correct variant calls were recovered

We suspect there are other genes where remapping recovered variants, and there may even be some that were lost (we have yet to notice any).
However, we did notice a _very_ slight increase in sensitivity and precision when we made the change.
