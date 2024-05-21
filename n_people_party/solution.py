import math

def sol(n):
    ways = [-1]*(n)

    def getWays(n):
        if n<0:
            return -1
        elif n==0:
            return 1
        elif n==1:
            return 2

        if ways[n-1]==-1:
            ways[n-1] = getWays(n-1)
            print(n, ways)
        if ways[n-2]==-1:
            ways[n-2] = getWays(n-2)
            print(n, ways)
        return ways[n-1]+ways[n-2]*(n-2)
    
    getWays(n)
print(sol(7))
