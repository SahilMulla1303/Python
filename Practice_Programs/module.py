'''
#1st method

import time

print(time.ctime())
print(time.localtime())
print("Sahil")
time.sleep(5)
print("Mulla")

'''

'''
#2nd method

import time as t

print("Sahil")
t.sleep(5)
print("Mulla")
print(t.ctime())
print(t.localtime())

'''

'''
#3rd method

from time import sleep,ctime,localtime

print("Sahil")
sleep(5)
print("Mulla")
print(ctime())
print(localtime())

'''

'''
#4th method

from time import *

print("Sahil")
sleep(5)
print("Mulla")
print(ctime())
print(localtime())

'''







