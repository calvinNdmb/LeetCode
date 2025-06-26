import time
start_time = time.time()
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        pass
    def isAnagram(self, s: str, t: str) -> bool:
        a={}
        b={}
        for i,j in zip(s,t):
            a[i]+=1
            b[i]=-1
        print(a,"\n",b)
        




if __name__ ==  '__main__':
    inputs=["act","pots"]
    s=Solution()
    print(s.isAnagram("test", "test"))

    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.10f}")
