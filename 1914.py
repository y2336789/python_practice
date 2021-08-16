def Hanoi(num, one, two, three):
    if num == 1:
        print(one,three); 
    else :
        Hanoi(num-1, one, three, two);
        print(one, three); 
        Hanoi(num-1, two, one, three);

num = int(input())
count = (2**num)-1
if num <= 20:
    print(count)
    Hanoi(num, 1, 2, 3);
elif num > 20:
    print(count)