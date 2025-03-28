#!/bin/bash
#SBATCH --job-name=coronary-rmats1
#SBATCH --partition=standard
#SBATCH --constraint=rivanna
#SBATCH --output=%x-%j.log
#SBATCH --mem=32G
#SBATCH --time=14:00:00
#SBATCH --account=cphg-millerlab-vip
#SBATCH --nodes=1
#SBATCH --ntasks=1

#Load rmats environment
module load miniforge
source activate 01_rmats_env

#Make output directories
mkdir -p ../03_outputs/prep/prep-directory1
mkdir -p ../03_outputs/post/post-directory1

#Run rmats analysis
python $CONDA_PREFIX/bin/rmats.py --b1 ../01_inputs/bam_files/isch-bams1.txt \
        --b2 ../01_inputs/bam_files/ctrl-bams1.txt \
        --gtf /sfs/gpfs/tardis/project/cphg-millerlab/CAD_QTL/coronary_QTL/transcriptome/LeafCutter/STAR/gencode.v37.annotation.gtf \
        --tmp ../03_outputs/prep/prep-directory1 \
        --od ../03_outputs/post/post-directory1 \
        --readLength 150 \
        --task both

