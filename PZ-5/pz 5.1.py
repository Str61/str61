def summary(digit):
    n = abs(n)
    if n == 0:
        return 0
    else:
        return n % 10 + summary(n // 10)

def tytyty(i):
     http = 0
     while i > 0:
         i -= summary(i)
         http += 1
     return http


sum = int(input("Введите число: "))
ii = tytyty(sum)
print(ii)