#!/bin/bash
val=$(echo $(sed -n 7p trees.txt))
str=$(echo ${val:37})
str2=$(echo $(cut -d "(" -f2- <<< $str))
final="($str2"
echo $final
