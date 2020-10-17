#!/bin/bash
start=1
p=p
q=q
for((i=1;i<=9;i++))
do
end=`expr $start + 400`

endparse=`expr $end + 1`
sed -n "$start,$end$p;$endparse$q" seqfile.txt_TRUE.phy > "t$i.seq"
start=`expr $end + 3`
done
end=`expr $start + 400`
sed -n "$start,$end$p" seqfile.txt_TRUE.phy > "t$i.seq"

