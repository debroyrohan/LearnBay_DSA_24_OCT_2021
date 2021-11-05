class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        result = False
    
        while("#" in s and len(s) > 0):
            
            if(s.find("#") != 0):
                s = s[:s.find("#") - 1] + s[s.find("#")+1:]
                
            else:
                s = s.replace("#", '', 1)

        while("#" in t and len(t) > 0):
            
            if(t.find("#") != 0):
                t = t[:t.find("#")-1] + t[t.find("#")+1:]
                
            else:
                t = t.replace("#", '', 1)
        
        if(s == t):
            result = True
        return result
        
