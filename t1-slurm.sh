#!/bin/bash
#SBATCH --job-name=01_slurm_test
#SBATCH --partition=standard
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --constraint=rivanna
#SBATCH --output=02-test-%j.log
#SBATCH --mem=2G
#SBATCH --time=00:05:00
#SBATCH --account=cphg-millerlab-vip


module load anaconda

conda activate 01_rmats_env

echo "conda environment activated"

which python
which rmats.py
