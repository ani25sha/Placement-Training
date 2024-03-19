class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        #Binary list formation
        l=list(bin(n))
        l=l[2:]
        for i in range(1,len(l)):
            if l[i-1]==l[i]:
                #return false on equal check
                return False
        return True