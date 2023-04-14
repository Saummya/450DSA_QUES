'''
Question

Move all negative numbers to beginning and positive to end with
 constant extra space.
 
An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

Examples : 

Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
'''

arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]

#arr.sort()  
#print(arr)

#t.c.= O(nlogn)

#two pointer method.

n=len(arr)

left=0
right=n-1

while left<=right:
    if arr[left]<0 and arr[right]<0:
        left+=1
        
    elif arr[left]>0 and arr[right]<0:
        arr[left],arr[right]=arr[right],arr[left]
         
        left+=1
        right-=1
        
    elif arr[left]>0 and arr[right]>0:
        right-=1
        
    else:
        left+=1
        right-=1
        
print(arr)
        
    
    
    
    
    
    
    
    
    


