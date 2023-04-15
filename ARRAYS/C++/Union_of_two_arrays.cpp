/*
Problem:- Union of two arrays
Problem link:- https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1
*/

class Solution{
    public:
    //Function to return the count of number of elements in union of two arrays.
    // time complexity O(n*m)
    /*int doUnion(int a[], int n, int b[], int m)
    {
        int cnt=m+n;
        for(int i=0;i<n;i++) 
        {
            for(int j=0;j<m;j++)
            {   
                if(a[i]==b[j])
                  cnt--;
            }
        }
        return cnt;
    }*/
    // time complexity O(n+m)
    int doUnion(int a[], int n, int b[], int m)  {
        unordered_map<int,int>mp;
        for(int i=0; i<n; i++)
        {
            mp[a[i]];
        }
        for(int i=0; i<m; i++)
        {
            mp[b[i]];
        }
        return mp.size();
    }
};