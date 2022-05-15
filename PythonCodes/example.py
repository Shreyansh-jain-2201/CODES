s = "Wearehere"
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
s = s.upper()
o = ''
for i in range(len(s)):
    o += alp[alp.index(s[i])-4]
print(o)