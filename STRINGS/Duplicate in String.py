'''
Ques:
    Print all the duplicate characters in a string
    
    
EXAMPLE: 
Input: S = “geeksforgeeks”
Output:

e, count = 4
g, count = 2
k, count = 2 
s, count = 2
'''

#HASHING

def duplicates(Str):
    dup={}
    for i in range(len(Str)):
        if Str[i] in dup:
            dup[Str[i]]+=1
        else:
            dup[Str[i]]=1
            
    for i, j in dup.items():
        if j>1:
            print(str(i)+", count= " +str(j))
S = "geeksforgeeks "          
duplicates(S)
            
            
