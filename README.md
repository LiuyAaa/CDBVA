# CDBVA
_A Control Flow Detection Method Based on Basic Block Vulnerability_

**Runtime Environment：**

Ubuntu 16.04 with the 4.15 kernel；

LLVM 4.0；

Python >= 3.0.

**Program Harden:**

Run _Preprocess-CDBVA.sh_.

**Fault Injection:**

Enter in the program directory.

./auto.sh program to be injected; Program parameters; Number of runs; Fault injection method; Daemon detection time interval;

for example:

![image](https://github.com/LiuyAaa/CDBVA/assets/28710052/e0b66377-5159-49c4-9c26-19c14f165885)

The program name to inject the fault is: qsort_ smallcfsig

The parameters of the program are: input.dat

The number of runs of the program is: 10

The method of fault injection is: p (there are two fault injection methods: p and r)

The running time interval of the detection program to detect whether the program has entered a dead cycle is: 60s

Count the number of detected errors:

	python3  find_error_statistics.py inject.output

for example：

![image](https://github.com/LiuyAaa/CDBVA/assets/28710052/e716c7c5-098e-4d6a-a61d-f7070076a379)




