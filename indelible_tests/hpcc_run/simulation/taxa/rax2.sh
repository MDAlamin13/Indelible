#!/bin/bash
#SBATCH --time=05:00:00
ran=7878
for((i=600;i<=600;i+=100))
do
cd "T$i"
for((j=4;j<=10;j++))
do
ran=`expr $ran + 23965`
./raxmlHPC -p $ran -m GTRCAT -s "t$j.seq" -n "t$j.rml"
done
cd ..
done 

scontrol show job $SLURM_JOB_ID     ### write job information to SLURM output file
js -j $SLURM_JOB_ID                 ### write resource usage to SLURM output file (powetools command)