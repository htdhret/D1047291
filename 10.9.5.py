def pyramid(n):
    for i in range(n+1):
        print(' '*(n-i)+'*'*(2*i-1))

pyramid(9)