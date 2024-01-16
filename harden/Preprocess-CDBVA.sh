#!/bin/bash 
# Processing source programs, splitting basic blocks, and inserting code
cp $1 ./${1##*/}

prog_dir=${1%/*}
echo $prog_dir
filename=${1##*/}
echo $filename
/home/yy2/Desktop/llvm/build/bin/clang -S -g -emit-llvm $filename -o ${filename%.c}.ll
/home/yy2/Desktop/llvm/build/bin/opt -load /home/yy2/Desktop/llvm/build/lib/AddGlobalSig.so -AddGlobalSig -S ${filename%.c}.ll -o ${filename%.c}.ll
/home/yy2/Desktop/llvm/build/bin/opt -load /home/yy2/Desktop/llvm/build/lib/Index.so -Index -disable-output ${filename%.c}.ll 2> allindex.txt
python3 sort.py > index.txt
rm allindex.txt
echo 'index.txt done'
for line in `cat index.txt`
do
	/home/yy2/Desktop/llvm/build/bin/opt -load /home/yy2/Desktop/llvm/build/lib/SplitBlock.so -SplitBlock -S -index $line ${filename%.c}.ll -o  ${filename%.c}.ll 
done
echo 'split done'
/home/yy2/Desktop/llvm/build/bin/opt -load /home/yy2/Desktop/llvm/build/lib/HARDEN.so -HARDEN -S ${filename%.c}.ll -o harden.ll
echo 'harden done'
/home/yy2/Desktop/llvm/build/bin/clang -lm harden.ll -o ${filename%.c}_CDBVA

rm harden.ll
echo 'all done'
