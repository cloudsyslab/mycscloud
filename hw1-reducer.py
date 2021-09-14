#!/usr/bin/env python
import sys
Cur_Addr = None; Cur_Count = 0
Max_Addr = None; Max_Count = 0
MaxCrimeList = []; CrimeList = []

for line in sys.stdin:
    line=line.strip()
    addr, crime = line.split("\t") 
    if addr == Cur_Addr: 
        Cur_Count +=1 
        CrimeList.append(crime)
    else:
        if Cur_Count > Max_Count:
            Max_Count = Cur_Count
            Max_Addr = Cur_Addr		
            MaxCrimeList = CrimeList
        Cur_Addr = addr
        Cur_Count = 1
        CrimeList = []
        CrimeList.append(crime)

# after end of for loop
if Cur_Count > Max_Count:
    Max_Count = Cur_Count
    Max_Addr = Cur_Addr
    MaxCrimeList = CrimeList

print ("%s\t%s" % (Max_Addr, MaxCrimeList))


