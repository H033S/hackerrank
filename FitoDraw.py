global Max 
global ft_l
global ft_r

lsb = lambda x: x&(-x)

def update(ft, k, v):
    while k <= Max:
        ft[k] += v
        k += lsb(k)

def query(ft, k):
    sum = 0
    
    while k > 0:
        sum += ft[k]
        k -= lsb(k)

    return sum 
                         

if __name__ == "__main__":
    Max = 100003
    ft_l = [0]*Max
    ft_r = [0]*Max

    tc = int(input())

    for i in range(tc):
        a, b = list(map(int, input().split()))

        update(ft_l, a, 1)
        update(ft_r, b, 1)

        query_l = query(ft_l, a - 1) - query(ft_r, a)
        query_r = query(ft_l, b - 1) - query(ft_r, b)


        print(query_l + query_r)