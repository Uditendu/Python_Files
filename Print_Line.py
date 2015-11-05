"""Module to Check for a particular word and print sentences containing that word
"""
import Count_Occurance

def print_line(txt, check):
    split = txt.split('.')
    l = len(split)
    i = 0
    s=[]
    while i<l:
        n = Count_Occurance.count_occurance(split[i],check)
        k = int(n[len(n)-1])
        if k>0:
            s.append(split[i])
        i+=1
    return s