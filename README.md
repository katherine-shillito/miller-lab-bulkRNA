# Differential Alternative Splicing in Ischemic vs Healthy Coronary Artery Tissue
## Project Overview
This project investigates the role of alternative splicing in coronary artery disease through analysis of differential splicing events between ischemic and healthy coronary artery tissue sample bulk RNA sequencing data. The computational tool rMATS-Turbo is used to identify and quantify differential splicing of five event types:
1. Skipped Exon
2. Mutually Exclusive Exons
3. Alternative 5' Splice Site
4. Alternative 3' Splice Site
5. Retained Intron

## Project Directory Structure

```
01_coronary-rmats/
|-- 00_test-directory/
|   |-- 01_test-inputs/
|   |   |-- test-ctrl-bams.txt
|   |   `-- test-isch-bams.txt
|   |-- 02_test-scripts/
|   |   |-- test1-rmats.sh
|   |   |-- test1-rmats-icr-65904406.log
|   |   |-- test2-rmats.sh
|   |   `-- test2-icr-594306.log
|   |-- 03_test-outputs/
|   |   |-- test-post-outputs/
|   |   `-- test-prep-outputs/
|   `-- 04_test-analysis/
|       `-- icr-eda-test2.Rmd
|-- 01_inputs/
|   |-- bam_files/
|   `-- metadata/
|       |-- ctrl-mdf-filtered1.txt
|       |-- isch-mdf-filtered1.txt
|       `-- metadata_RNA_022421.txt
|-- 02_scripts/
|   |-- coronary-rmats1.sh
|   |-- write-bam-lists.py
|   |-- coronary-rmats1-594713.log
|   `-- README.md
|-- 03_outputs/
|   |-- prep/
|   |   `-- prep-directory1/
|   `-- post/
|       `-- post-directory1/
`-- 04_analysis/
    |-- coronary-rmats1-BED.Rmd
    |-- coronary-rmats1-eda.Rmd
    `-- rMATStoBED.py
```

## rMATS-Turbo Installation
#### rMATS-Turbo requires the following dependencies:
Required:
- Python(3.6.12 or 2.7.15)
- BLAS, LAPACK
- GNU Scientific Library (GSL 2.5)
- GCC (>=5.4.0)
- gfortran (Fortran 77)
- CMake (3.15.4)
Optional:
- PAIRDISE
- DARTS
- Samtools
- STAR

#### Install rMATS turbo with all necessary dependencies and create a dedicated conda environment for the project by executing the following commands in the project's root directory:
1. Create environment and install all software

   ```conda create -n 01_rmats_env -c conda-forge -c bioconda rmats```

2. Activate environment

   ```module load miniforge  ```

   ```source activate 01_rmats_env```

## Prepare Input Files
#### BAM File Lists
The python script `write-bam-lists.py` generates comma separated lists of BAM file paths for each sample group:
- `isch-bams1.txt` - 7 Ischemic Samples
- `ctrl-bams1.txt` - 21 Control Samples

#### Reference Annotation
The GTF file `gencode.v32.annotation.gtf` contains transcript annotations needed for the splicing analysis. This is the same reference file used to align BAM files.

## Run rMATS-Turbo
The analysis is run via the SLURM script `coronary-rmats.sh` on an HPC cluster.

#### Recommended Compute Resources
Based on test runs with the dataset containing 28 BAM files:
- Memory: 5-10 GB
- Nodes: 1
- CPUs per Node: 2
- Walltime: 10-15 hours

#### Analysis Steps
1. Prepare environment:

   ```module load miniforge  ```

   ```source activate 01_rmats_env```

2. Create output directories for the prep step temporary output files and post step final output files:
   
   ```mkdir -p ../03_outputs/prep/prep-directory1```
   
   ```mkdir -p ../03_outputs/post/post-directory1```
   
3. Execute rMATS:

   ```
   python $CONDA_PREFIX/bin/rmats.py --b1 ../01_inputs/bam_files/isch-bams1.txt \
        --b2 ../01_inputs/bam_files/ctrl-bams1.txt \
        --gtf ../01_inputs/gencode.v37.annotation.gtf \
        --tmp ../03_outputs/prep/prep-directory1 \
        --od ../03_outputs/post/post-directory1 \
        --readLength 150 \
        --task both
   ```

#### Parameter Descriptions:
Required Parameters
- --b1           path to sample group 1 text file
- --b2           path to sample group 2 text file
- --gtf          path to gene annotation file
- --tmp          path to temporary prep step output directory
- --od           path to final post step output directory
- --readLength   the RNA-seq data read length is 150 base pairs
- --task         run both the prep and post successively with one script rather than separately

## Output File Analysis
An exploratory data analysis of the rMATS-turbo output is found in `coronary-rmats1-eda.Rmd`. 

The `AS_Event_Name.MATS.JCEC.txt` files are used which contains data for all alternative splicing events, separated by event type, which were identified using two calculation methods:
1. Exon counts = quantification of reads containing a given exon abundance
2. Junction counts = quantification of reads spanning exon-exon junctions

#### Data Filtering
The data was filtered to identify statistically significant and biologically relevant differential splicing events. 

1. Read coverage in both sample groups greater than 10
2. Events with extreme average PSI values in both sample groups (>= 0.05 in both or <= 0.95 in both)
3. FDR value less than 0.01
4. Absolute Delta PSI Value greater than 0.1 (difference in splicing > 10%)

Filtered Dataset:
- 505 events total spanning 430 different genes
