# Differential Alternative Splicing Events in Ischemic vs Control Coronary Artery Tissue

## Project Overview
This project aims to analyze differential alternative splicing between ischemic and control samples of coronary artery tissue from bulk RNA sequencing data. rMATS-Turbo is used to identify five basic splicing events (skipped exons, alternative 5' splice sites, alternative 3' splice sites, mutually exclusive exons, and retained introns) and quantify differential splicing between the two sample groups. 

## rMATS-Turbo
rMATS Turbo must be installed with several required dependencies:
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

Create a conda environment for the project and install all rMATS-Turbo and all of its required dependencies in one step in the project directory:

conda create -n 01_rmats_env -c conda-forge -c bioconda rmats

Activate the conda environment:

conda activate 01_rmats_env

## Usage
Create slurm script to run rMATS analysis using UVA research computing.

nano ic-rmats1.sh

### Input Files
1. BAM Files with RNA Sequencing Data
- Data filtered to remove explant samples and  include only coronary_artery tissue.
- Sample Group 1: Ischemic Samples
- Sample Group 2: Control Samples
- Comma separated lists of BAM files for sample groups obtained from Star_Pass2 directory: ischemic_bam_list.txt, control_bam_list.txt
2. Transcript Annotation GTF File
- gencode.v32.annotation.gtf

### Create Output Directories
mkdir 02_prep_directory
- output of prep step; temporary directory
mkdir 03_post_directory
- output of post step; rmats output text files

### Run Analysis
python $CONDA_PREFIX/bin/rmats.py --b1 ../01_inputs/bam_files/isch-bams1.txt \
        --b2 ../01_inputs/bam_files/ctrl-bams1.txt \
        --gtf /sfs/gpfs/tardis/project/cphg-millerlab/CAD_QTL/coronary_QTL/transcriptome/LeafCutter/STAR/gencode.v37.annotation.gtf \
        --tmp ../03_prep-outputs/prep-directory1 \
        --od ../04_post-outputs/post-directory1 \
        --readLength 150 \
        --task both



- Read length is a required argument: 150 Base Pairs
- rMATS-turbo prep and post steps are completed with a single run
- Alternative splicing events involving novel/unannotated splice sites will be identified (optional argument)


