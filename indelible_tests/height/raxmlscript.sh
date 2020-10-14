#!/bin/bash
ran=34635 
for((i=2;i<=9;i++))
do
name="h$i.5"
cd $name
for((j=1;j<=10;j++))
do
ran=`expr $ran + 2345`
raxmlHPC -p $ran -m GTRCAT -s "t$j.seq" -n "t$j.rml"
done
cd ..
done

