#!/bin/bash
#SBATCH --time=05:00:00
for((i=100;i<=800;i+=100))
do
cd "T$i"
for((j=1;j<=10;j++))
do
./FastTree -nt < "t$j.seq" > "t$j.fast"
done
cd ..
done 

scontrol show job $SLURM_JOB_ID     ### write job information to SLURM output file
js -j $SLURM_JOB_ID                 ### write resource usage to SLURM output file (powetools command)