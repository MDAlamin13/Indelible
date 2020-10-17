#!/bin/bash
#SBATCH --time=05:00:00
ran=85632
for((i=100;i<=800;i+=100))
do
cd "s$i"
for((j=1;j<=10;j++))
do
ran=`expr $ran + 2345`
./raxmlHPC -p $ran -m GTRCAT -s "t$j.seq" -n "t$j.rml"
done
cd ..
done 

scontrol show job $SLURM_JOB_ID     ### write job information to SLURM output file
js -j $SLURM_JOB_ID                 ### write resource usage to SLURM output file (powetools command)