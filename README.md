# Ischemic vs Control Alternative Splicing Events

## Overview
The project aims to identify differential alternative splicing events between ischemic and control samples of bulk RNA sequencing data using rMATS-Turbo. The program identifies and quantifies five basic alternative splicing events; skipped exons, alternative 5' splice sites, alternative 3' splice sites, mutually exclusive exons, and retained introns. A statistical analysis is used to identify differential splicing between the two sample groups.

## Installation
Required Dependencies:
- Python(3.6.12 or 2.7.15)
- BLAS, LAPACK
- GNU Scientific Library (GSL 2.5)
- GCC (>=5.4.0)
- gfortran (Fortran 77)
- CMake (3.15.4)

Optional Dependencies:
- PAIRDISE
- DARTS
- Samtools
- STAR

Install rMATS-Turbo and all required dependencies within a conda environment, specific to the project:
conda create -n 01_rmats_env -c conda-forge -c bioconda rmats

Activate Conda Environment:
conda activate 01_rmats_env

## Usage
Run analysis in	slurm script to	use UVA	HPC.

### Input Files
1. BAM Files with RNA Sequencing Data
- Data filtered to remove explant samples and  include only coronary_artery tissue.
- Sample Group 1: Ischemic Samples
- Sample Group 2: Control Samples with no lesions
- Comma separated lists of BAM files for sample groups obtained from Star_Pass2 directory: ischemic_bam_list.txt, control_bam_list.txt
2. Transcript Annotation GTF File
- Obtained from reference_genomes/hg38 directory: hg38.fa.sa.gz

### Create Output Directories
mkdir 02_prep_directory
- will hold output of prep step; temporary directory
mkdir 03_post_directory
- will hold output of post step

### Run Analysis
python rmats.py --b1 ischemic_bam_list.txt --b2 control_bam_list.txt --gtf hg38.knownGene.gtf --tmp 02_prep_directory --od 03_post_directory --readlength 150 --task both --novelSS
- Read length is a required argument: 150 Base Pairs
- Both prep and post steps of rMATS-turbo are run in a single run
- Alternative splicing events involving novel/unannotated splice sites will be identified (optional argument)



