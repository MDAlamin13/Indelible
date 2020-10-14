#!/bin/bash

for((i=2;i<=9;i++))
do
cd "h$i.5"
indelible
./extract.sh
cd ..
done
