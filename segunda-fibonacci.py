def fibonacci(n):
    if n < 0:
        return False
    elif n == 0 or n == 1:
        return True
    else:
        num1 = 0
        num2 = 1
        while num2 < n:
            aux = num1
            num1 = num2
            num2 = num2 + aux
        return num2 == n


n = 34
if fibonacci(n):
    print(f"O numero {n} pertence a sequência de fibonacci")
else:
    print(f"O numero {n} não pertence a sequência de fibonacci")



