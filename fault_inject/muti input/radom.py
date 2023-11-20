import random                                   #导入随机函数
import sys
n=int(sys.argv[1])

a=[random.randint(1,100000000)for i in range(n)]
a=list(map(str,a))

f=open("./input"+sys.argv[2]+".dat",'a+')
for i in a:
    f.write(i)
    f.write("\n")                               #每个数字一行
f.close()
