# fibonacci(0) = 0 : 1번, 1 : 0번
# fibonacci(1) = 0 : 0번, 1 : 1번
# fibonacci(2) = fibonacci(1) + fibonacci(0) -> 0 : 1번, 1 : 1번
# fibonacci(3) = fibonacci(2) + fibonacci(1) -> 0 : 1번, 1 : 2번
# fibonacci(4) = fibonacci(3) + fibonacci(2) -> 0 : 2번, 1 : 3번
# fibonacci(5) = fibonacci(4) + fibonacci(3) -> 0 : 3번, 1 : 5번

zero = [1, 0, 1] # 여기에 1, 2, 3, 5, 8 ... 추가해 나갈 예정
one = [0, 1, 1] # 여기에는 2, 3, 5, 8, ... 추가해 나간다.

def fibonacci(num):
    if len(zero) <= num:
        for i in range(len(zero), num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])    
    print(zero[num], one[num]);

a = int(input())

for i in range(a):
    num = int(input())
    fibonacci(num)