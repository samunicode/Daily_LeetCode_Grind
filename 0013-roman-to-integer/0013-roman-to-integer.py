class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        value, l = 0, len(s)
        s = s + 'F'
        for i in range(0, l):
            if s[i+1] != 'F' and hmap[s[i]] >= hmap[s[i+1]]:
                value += hmap[s[i]]
            elif  s[i+1] != 'F' and hmap[s[i]] < hmap[s[i+1]]:
                value -= hmap[s[i]]
            elif s[i+1] == 'F':
                value += hmap[s[i]]
        
        return value