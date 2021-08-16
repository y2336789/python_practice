def RecursiveFactorial(n):
    if(n==0):
        return 1;
    else :
        return n * RecursiveFactorial(n-1);

print(RecursiveFactorial(int(input())))
