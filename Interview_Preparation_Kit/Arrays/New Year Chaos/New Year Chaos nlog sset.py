from sortedcontainers import SortedSet 

def minimumBribes(q):
    a = SortedSet(1,2,3,4,5)
    
    
    
"""
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
"""

a = SortedSet([1, 2, 3, 4, 5])

print(a.count(lambda x: x < 4))
