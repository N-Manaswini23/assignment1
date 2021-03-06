# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWc2yWZbvszs5Q0SFJ6nhZgtwPTh4V-X
"""

from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
import random 
import array as event
import matplotlib.pyplot as plt
import math
import numpy as np
arr=event.array('f',[0,0,0,0,0,0,0])
#function to calculate n!
def prod(n):
   fact = 1
   for x in range(1 , n + 1):
     fact = fact * x
   return fact

#function to calculate binomial coefficient(ncr)
def bino(n,r):
   bin_coeff = prod(n) / (prod(n-r)*prod(r))
   return bin_coeff

def prob(n,r):
   probab = bino(n,r)/pow(2,6)
   return probab
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


max=arr[0]/x
j=0

for i in range(7):
    arr[i]=arr[i]/x
    if max<arr[i]:
       max=arr[i]
       j=i

print(f'probability that at the event occurs 0 times out of 6 is:{arr[0]}\n')
print(f'probability that at the event occurs 1 times out of 6 is:{arr[1]}\n')
print(f'probability that at the event occurs 2 times out of 6 is:{arr[2]}\n')
print(f'probability that at the event occurs 3 times out of 6 is:{arr[3]}\n')
print(f'probability that at the event occurs 4 times out of 6 is:{arr[4]}\n')
print(f'probability that at the event occurs 5 times out of 6 is:{arr[5]}\n')
print(f'probability that at the event occurs 6 times out of 6 is:{arr[6]}\n')

maxim=prob(6,0)
k=0

for i in range(7):
   if maxim<prob(6,i):
      maxim=prob(6,i)
      k=i


print(f'(simulation)most likely outcome has probability:{max}')
print(f'This corresponds to X={j}.Therefore P(X={j}) is most likely outcome(simulation)\n')
print(f'(theoretrical)most likely outcome has probability:{maxim}')
print(f'This corresponds to X={k}.Therefore P(X={k}) is most likely outcome(theoretrical)\n')

x=[0,1,2,3,4,5,6]
h=[arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6]]
plt.bar(x,h,0.25)
plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Simulation")
plt.show()

#Theoretrically P(x=k)=6Ck(1/2)^6
m=[0,1,2,3,4,5,6]
n=[prob(6,0),prob(6,1),prob(6,2),prob(6,3),prob(6,4),prob(6,5),prob(6,6)]
plt.bar(m,n,0.25)

plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Theoretrical probability")

plt.show()