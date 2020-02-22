import math as m

class D(dict):
    def __getitem__(self, key):
        if key not in self.keys(): 
            return 'Not found'
        value = super().__getitem__(key)
        return '{}={}'.format(key,value)

n = int(input())
d = D()

for x in range(n):
    st = input().split()
    d.update({st[0]:st[1]})

#print(d[st])

while 1:
    try:
        s = input()
        print(d[s])
    
    except(EOFError):
        break