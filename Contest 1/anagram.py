class Solution:

    def isAnagram(self, S):
        d={}
        for i in S:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        c=0
        for i,j in d.items():
            if j%2!=0:
                c+=1
        if c>1:
            return 0
        return 1    