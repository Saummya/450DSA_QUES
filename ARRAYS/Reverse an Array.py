

'''
Write a program to reverse an array or string.

Given an array (or string), the task is to reverse the array/string.
Examples : 
 

Input  : arr[] = {1, 2, 3}
Output : arr[] = {3, 2, 1}

Input :  arr[] = {4, 5, 1, 2}
Output : arr[] = {2, 1, 5, 4}
'''

A = [1, 2, 3, 4, 5, 6]
print(A)

'''
ways to reverse an array;
1. Using another array
2. Using the same array
3. Recursion 
'''

#1. Using another array

b=[]
for i in range(len(A)-1,-1,-1):
    b.append(A[i])
    
#print(b)

# time complexity- O(n)
# space complexity- O(n)

#2. Using the same array

def reverseArray(A,start,end): #0-5, 1-4, 2-3
    while start<end:
        A[start],A[end]=A[end],A[start]
        start+=1
        end-=1
        
reverseArray(A,0,5)
print("reversed Array")
print(A)

#time complexity- O(n)
#space complexity- O(1)


        # 3. Recursion
        
def reverseArray1(A,start,end): #[1,2,3,4,5]
    if start>=end:
        return
    A[start],A[end]=A[end],A[start]
    reverseArray1(A,start+1,end-1)
    
reverseArray1(A,0,5)
print("reverse array")
print(A)

def rev(A):
    print(A[::-1])
    
print("using list slicing")
print(A)
    
 
