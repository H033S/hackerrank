class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        it = self.__elements
        l = len(self.__elements)
        _ = 0


        for i in range(l):
            for j in range(i+1,l):
                _ = max(_, abs( it[i] - it[j] )) 
        
        d.maximumDifference =  _
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)