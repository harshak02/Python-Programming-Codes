#!/bin/python

import math
import os
import random
import re
import sys

#n = int(raw_input())-> used only in the python 2.x version

if __name__ == '__main__':
    n = input()
    n = int(n)
    
    if(n%2!=0) :
        print("Weird")
        
    elif((n%2==0) and (n>=2) and (n<=5)) :
        print ("Not Weird")
        
    elif ((n%2==0) and (n>=6) and (n<=20)) :
        print ("Weird")
        
    else :
        print ("Not Weird")

