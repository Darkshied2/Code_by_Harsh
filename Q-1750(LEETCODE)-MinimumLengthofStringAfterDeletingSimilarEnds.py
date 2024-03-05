class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1
        while i<=j:
            if i==j and s[i]==s[j]:
                return 1
            if s[i]!=s[j]:
                return j-i+1
            e1,e2=i,j
            while e1<j and s[e1]==s[i]:
                e1+=1
            i=e1
            while e2>=0 and s[e2]==s[j]:
                e2-=1
            j=e2
        return 0
