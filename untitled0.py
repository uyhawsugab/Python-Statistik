# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O-ww7BYWa63_LtGRaeJBKayC8r22Ot_g
"""

def bubblesSort(arr):
  x = len(arr)
 

  for i in range(x-1):
    for j in range(0, x-i-1):

      if arr[j] > arr[j+1]:
          arr[j], arr[j+1] = arr[j+1], arr[j]



arr = []
y=range(10) 
for i in y:
  arr.append(int(input()))

bubblesSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
  print("%d"% arr[i]),

arr=[]
y = range(10)

for i in y:
  arr.append(int(input()))

x = len(arr)
get_jumlah = sum(arr)
mean = get_jumlah / x
print("Mean dari array adalah :" + str(mean))

arr = []
y = range(10)

for i in y:
  arr.append(int(input()))

x = len(arr)
arr.sort()

if x % 2 == 0:
  median1 = arr[x//2]
  median2 = arr[x//2 - 1]
  median = (median1 + median2)/2
else:
  median = arr[x//2]
print("Nilai Median : "+str(median))

from collections import Counter

arr = []
y = range(10)

for i in y:
  arr.append(int(input()))

x = len(arr)

dataModus = Counter(arr)
getData = dict(dataModus)
modus = [
         z for z, 
         c in getData.items()
         if c == max(list(dataModus.values()))
]

if len(modus) == x:
  getData = "Tidak ada Modus yang muncul"
else :
  getData = "Modus adalah " +','.join(map(str,modus))


print(getData)

arr = []
y = range(10)

for i in y:
  arr.append(int(input()))

x = min(arr)

print("Angka Terkecil adalah " + str(x))

arr = []
y = range(10)

for i in y:
  arr.append(int(input()))

x = max(arr)

print("Angka Terbesar adalah " + str(x))

arr = []
y = range(10)

for i in y:
  arr.append(int(input()))

x1 = max(arr)
x2 = min(arr)
rentangData = x1 - x2;

print("Rentang data dari deret adalah " + str(rentangData))

def mean(arr):
  x = len(arr)
  mean = sum(arr) / x
  return mean
  


arr = []
temp = []

for i in range(0, 5):
  arr.append(int(input()))


for x in range(len(arr)):
    minus = arr[x] - mean(arr)
    if (minus < 0):
      temp1 = minus * -1
      temp.append(temp1)   
    else:
      temp.append(minus)   
    print(temp)
    

resultFix = sum(temp)/len(arr)
print(arr)



print("mean % s "% mean(arr))

print("deviasi " + str(resultFix))

import math

def mean(arr):
  x = len(arr)
  mean = sum(arr) / x
  return mean


arr = []
temp = []


for i in range(0,10):
  arr.append(int(input()))

for x in range(len(arr)):
    minus = arr[x] - mean(arr)
    if (minus < 0):
      temp1 = (minus * -1) ** 2
      temp.append(temp1)   
    else:
      temp2 = minus ** 2
      temp.append(temp2)
    print(temp)

resultVar = sum(temp)*10 / (len(arr) * (len(arr) - 1))
resultFix = math.sqrt(sum(temp))/math.sqrt(len(arr)-1)
print(arr)



print("mean % s "% mean(arr))

print("Varian adalah " + str(resultVar))

print("standard deviasi " + str(resultFix))