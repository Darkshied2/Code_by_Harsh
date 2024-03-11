        ans=""
        for i in order:
            c=s.count(i)
            if i in s:
                ans+=(i*c)
        for i in s:
            c=s.count(i)
            if i not in ans:
                ans+=(i*c)
            
        return ans
        
