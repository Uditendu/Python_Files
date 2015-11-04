"""Module to count how many times check appears in a String
"""
def count_occurance(txt, check):
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-123456789'
    txt+=' '
    l = len(check)
    n=0
    i=0
    j=0

    while i<(len(txt)-l+1):
        if txt[i]==check[0]:
            if txt[i:i+l]==check and txt[i-1].upper() not in Alphabet and txt[i+l].upper() not in Alphabet:
                n+=1
                i+=l
            else:
                i+=1
        else:
            i+=1
    return "No. of Occurance of "+check+"="+str(n)