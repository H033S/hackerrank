global s
global lazy

def update(id, l, r, x):
    if not (r - l):
        s[id] += x
    else:
        lazy[id] += x
        s[id] += x

def shift(id, l, r):
    mid = (l + r) >> 1

    update(id<<1, l, mid, lazy[id])
    update(id<<1|1, mid + 1, r, lazy[id])
    lazy[id] = 0

def increase(x, y, v, id, l, r):
    if x > r or l > y:
        return
    if x <= l <= r <= y:
        update(id, l, r, v)
        return
    
    shift(id, l, r)

    mid = (l + r) >> 1
    increase(x, y, v, id<<1, l, mid)
    increase(x, y, v, id<<1|1, mid + 1, r)
    s[id] = max(s[id << 1], s[id << 1|1])


def arrayManipulation(n, queries):    
    for q in queries:
        increase(q[0], q[1], q[2], 1, 0, n)    

    return s[1]
    #return query(1, n, 0, 0, n)  

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []
    s = [0]*(4*n)
    lazy = [0]*(4*n)

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
