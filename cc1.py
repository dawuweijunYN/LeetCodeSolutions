import sys
import os

def checkDifferent(iniString):
    # write code here
    for i in range(len(iniString)):
        for j in range(i+1,len(iniString)):
            if iniString[i] == iniString[j]:
                print("False")
                return False
    print("True")
    return True

checkDifferent("asdfghjkl")