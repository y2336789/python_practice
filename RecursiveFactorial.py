def RecursiveFactorial(n):
    if(n==0):
        return 1;
    else :
        return n * RecursiveFactorial(n-1);

print("1! = ", RecursiveFactorial(1));
print("2! = ", RecursiveFactorial(2));
print("3! = ", RecursiveFactorial(3));
print("4! = ", RecursiveFactorial(4));
print("9! = ", RecursiveFactorial(9));