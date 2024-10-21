#!/bin/bash
#SBATCH --job-name=t1-rmats-icr
#SBATCH --partition=standard
#SBATCH --constraint=rivanna
#SBATCH --output=%x-%j.log
#SBATCH --mem=32G
#SBATCH --time=5:00:00
#SBATCH --account=cphg-millerlab-vip
#SBATCH --nodes=1
#SBATCH --ntasks=1


#Load rmats environment
module load anaconda
conda activate 01_rmats_env

#Make output directories
mkdir -p ../03_prep-outputs/t1-prep-directory
mkdir -p ../04_post-outputs/t1-post-directory

#Run rmats analysis
python rmats.py --b1 ../01_inputs/t1-isch-bams.txt --b2 ../01_inputs/t1-ctrl-bams.txt --gtf ../01_inputs/hg38.knownGene.gtf --tmp ../03_prep-outputs/t1-prep-directory --od ../04_post-outputs/t1-post-directory --readLength 150 --task both





