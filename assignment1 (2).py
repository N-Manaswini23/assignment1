# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWc2yWZbvszs5Q0SFJ6nhZgtwPTh4V-X
"""

from scipy.stats import uniform
import random 
import array as event
import matplotlib.pyplot as plt
import math

arr=event.array('i',[0,0,0,0,0,0,0])


#1 if the event of binomial distribution has occured
#0 if the event of binomial distribution has not occured
#x counts total number of experiments
#event0/1/2/3/4/5/6 represents that the event has ocuured 0/1/2/3/4/5/6 times respectively out of 6 times.
x=0


while x<10000000:
    number=0
    for i in range(6):
        number+=random.randint(0,1)
    if number==0:
        arr[0]+=1
    elif number==1:
        arr[1]+=1
    elif number==2:
        arr[2]+=1
    elif number==3:
        arr[3]+=1
    elif number==4:
        arr[4]+=1
    elif number==5:
        arr[5]+=1
    elif number==6:
        arr[6]+=1
    x=x+1

print(f'probability that at the event occurs 0 times out of 6 is:{arr[0]/x}\n')
print(f'probability that at the event occurs 1 times out of 6 is:{arr[1]/x}\n')
print(f'probability that at the event occurs 2 times out of 6 is:{arr[2]/x}\n')
print(f'probability that at the event occurs 3 times out of 6 is:{arr[3]/x}\n')
print(f'probability that at the event occurs 4 times out of 6 is:{arr[4]/x}\n')
print(f'probability that at the event occurs 5 times out of 6 is:{arr[5]/x}\n')
print(f'probability that at the event occurs 6 times out of 6 is:{arr[6]/x}\n')

max=arr[0]
j=0

for i in range(6):
    if max<arr[i]:
       max=arr[i]
       j=i



print(f'most likely outcome has probability:{max/x}')
print(f'This corresponds to X={j}.Therefore P(X={j}) is most likely outcome\n')

x=[0,1,2,3,4,5,6]
h=[arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6]]
plt.bar(x,h,0.1)
plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Simulation\n")
plt.show()