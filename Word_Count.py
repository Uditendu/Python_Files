def word_count(txt):
    Alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ-123456789'
    txt+=' '
    i=0
    j=0
    if txt[0].upper() in Alphabet:
        n=1
    else:
        n=0

    while i< len(txt):
        if txt[i].upper() not in Alphabet:
            j=i
            while txt[j].upper() not in Alphabet:
                if j == (len(txt)-1):
                    break
                else:
                    j+=1
            if j == (len(txt)-1):
                    break 
            i=j
            n+=1
        elif i == (len(txt)-1):
            break
        else:
            i+=1
    return "no. of words=" + str(n)