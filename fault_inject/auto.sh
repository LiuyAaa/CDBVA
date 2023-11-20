#!/bin/bash
# Automatically inject faults and count the number of faults
# Usage: $0 $1Program to be injected $2Input file for the program $3Runs $4p/rFault injection method $5Daemon detection interval 
cp $1 ~/liu/testprograms/fault_inject
cp $2 ~/liu/testprograms/fault_inject
cd ~/liu/testprograms/fault_inject

#echo "get pc value"
#echo "file $1" > getpc.input
#echo "so getpc.py" >> getpc.input
#echo "getpcvalue "${2##*/} >> getpc.input
#gdb < getpc.input >/dev/null
#echo "get pc value done"

echo "file $1" > inject.input
echo "so start.py" >> inject.input
echo "set args ${2##*/}" >> inject.input
echo "start $5 $1 $3 $4 $6" >> inject.input
echo "gdb"
gdb < inject.input > inject.output
echo "correct"
./$1  ${2##*/} > inject.correct
# 把输入输出文件的编码格式改为 utf-8 否则python3 的 readline() 报错
 echo "convert corret output file"
vim inject.correct +"set fileencoding=UTF-8" +wq!
# 把输入输出文件的编码格式改为 utf-8 否则python3 的 readline() 报错
echo "convert output file"
vim inject.output +"set fileencoding=UTF-8" +wq!
echo "statistic"

python3 ./statistics/statistics.py inject.output inject.correct
