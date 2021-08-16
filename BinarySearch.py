def Recursive(num):
    if num <= 0:
        return;
    else:
        print("Recursive call! ", num);
        num -= 1; 
        Recursive(num);

Recursive(3)