'''
QUESTION:
    Maximum and minimum of an array using minimum number of comparisons
    
    Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

Examples:

Input: arr[] = {3, 5, 4, 1, 9}
Output: Minimum element is: 1
              Maximum element is: 9

Input: arr[] = {22, 14, 8, 17, 35, 3}
Output:  Minimum element is: 3
              Maximum element is: 35
              
'''
#Method 1--------------
A=[22, 14, 8, 17, 35, 3]
print(A)

A.sort()
print("sorted array",A)
print("max= ", A[-1])
print("min= ",A[0])

#time complexity= O(nlogn)

#Method2--------------
# [22, 14, 8, 17, 35, 3]
# min1=14->8->3
# max1=22->35

n=len(A)
if n==1:
    max1=A[0]
    min1=A[0]
    
else:
    if A[0]>A[1]:
        max1=A[0]
        min1=A[1]
    else:
        max1=A[1]
        min1=A[0]
        
for i in range(2,n):    # no of comparisons= 2*(n-2)+1=9 
    if A[i]>max1:
        max1=A[i]
    if A[i]<min1:
        min1=A[i]
        
print("max= ", max1)
print("min= ",min1)

#Method3------------------- -> best method 

# [22, 14, 8, 17, 35, 3]
#  [22, 14, 8, 17, 35]

#max1=22->35
#min1= 14->8->3

n=len(A)    # comparisons= 3*(n-1)/2 -->odd no. of elements

i=0          
if n%2==0: # comparisons= 3*(n-2)/2 +1=7  -->even no. of elements
    if A[0]>A[1]:
        max1=A[0]
        min1=A[1]
    else:
        max1=A[1]
        min1=A[0]
    i=2
else:
    max1=A[0]
    min1=A[0]
    
    i=1
while(i<n-1):        
    if A[i]>A[i+1]: 
        if A[i]>max1:
            max1=A[i]
        if A[i+1]<min1:
            min1=A[i+1]
    else:
        if A[i]>min1:
            min1=A[i]
        if A[i+1]<max1:
            max1=A[i+1]
            
    i+=2
print("max= ", max1)
print("min= ",min1)
    

        
       

    
    
    
 



        
        
        
        
    










