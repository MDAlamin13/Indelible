#!/bin/bash

for((i=2;i<=9;i++))
do
cd "h$i.5"
for((j=1;j<=10;j++))
do
FastTree -nt < "t$j.seq" > "t$j.fast"
done
cd ..
done 
