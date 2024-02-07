#!/bin/bash
#SBATCH --job-name=condition_checker_now
#SBATCH --begin=now
#SBATCH --partition=rondror
#SBATCH --dependency=singleton
#SBATCH --time=00:20:00
#SBATCH --mail-type=BEGIN,FAIL
#SBATCH --mail-user=jnoh2@stanford.edu
#
#SBATCH -o slurm/checker-now-%j.out
#SBATCH -e slurm/checker-now-%j.err

ml load python/3.6.1
python3 analyze_jobs.py   
