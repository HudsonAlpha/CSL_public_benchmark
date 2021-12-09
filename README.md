# CSL_public_benchmark
This repo is intended to provide a periodically-updated, public view into genome sequencing benchmarks managed by [HudsonAlpha's Clinical Services Lab (CSL)](https://clinicallab.org).
The benchmarking results primarily provide the CSL a systematic approach to evalute various reference genome, aligner, and variant caller combinations against each other.
All of the datasets we used for testing were generated at HudsonAlpha.
The short-read PCR-free datasets were generated using standard clinical processes in the CSL and are currently private datasets.
The long-read PacBio datasets were generated by the [Genome Sequencing Center](https://www.hudsonalpha.org/gsc/) and are publicly hosted through the Genome in a Bottle consortium (see below).

The benchmarks or "truth sets" themselves are large-scale publicly available benchmarks created for a handful of reference samples. 
Most of the benchmarks we use were generated by the [Genome in a Bottle (GIAB) Consortium](https://www.nist.gov/programs-projects/genome-bottle).

## Current status
This initial release just includes the final results files that are reviewed after the pipelines have completed.

## What is the pipeline?
The benchmarking pipeline itself is maintained in a private repo.
Briefly, it is a [snakemake](https://snakemake.readthedocs.io/en/stable/) pipeline that built around a systematic final evaluation that mostly uses [RTG vcfeval](https://github.com/RealTimeGenomics/rtg-tools) to measure sensitivity and precision.
The primary "wildcards" in this evaluation are the reference, the aligner, and the variant caller; with versioning where appropriate.
This allows us to quickly add new tools by defining new rules to run a particular tool (typically one per aligner or caller), and then evaluate in a standard way.
In general, we try to use docker images or conda environments when these are already available to increase downstream portability; however, these are not always available.

As a result, many rules are tied to our cluster ecosystem, either through modules and/or file paths to installed software.
Additionally, all the metadata (e.g. fastq pairs for a given sample) is tracked using an internal system.
This means that this pipeline, even if publically available, would definitely not run "out-of-the-box" for anyone outside of HudsonAlpha.
A _very_ long-term goal would be to create a public version that _can_ run out-of-the-box given user-provided metadata.

However, in the interest of transparency, we will be making efforts to clarify any questions about the implementation over time.
This will largely be driven by questions we receive from the community (i.e. create issues if you have questions, so we can begin tackling this).
Examples of things already on the TODO radar:

- Rules for aligners and callers
- Rules for evaluation
- Description/links to specific reference files
