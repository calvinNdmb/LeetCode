class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b={}
        for i in s:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for i in t :
            if i in b:
                b[i] += 1
            else:
                b[i] = 1
        try:
            for i in a: 
                b[i]-= a[i]
            for i in b :
                if b[i] != 0:
                    return False
            print (a,"\n",b)
        except KeyError:
            return False
        return True 

