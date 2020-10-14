#!/bin/bash

for((i=800;i<=800;i+=100))
do
cd "s$i"
indelible
./extract.sh
cd ..
done
